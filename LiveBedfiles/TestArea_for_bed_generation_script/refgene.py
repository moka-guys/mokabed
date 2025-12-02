#!/usr/bin/env python3
import argparse
import gzip
import io
import json
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - make dependency issues obvious at runtime
    yaml = None


def smart_open(path):
    if path.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"))
    return open(path, "r", encoding="utf-8")


# UCSC fields (16 columns):
# 0 bin, 1 name (transcript), 2 chrom, 3 strand, 4 txStart, 5 txEnd,
# 6 cdsStart, 7 cdsEnd, 8 exonCount, 9 exonStarts, 10 exonEnds,
# 11 score, 12 name2 (gene), 13 cdsStartStat, 14 cdsEndStat, 15 exonFrames
def parse_refgene_line(line):
    # split on any whitespace to be resilient to tabs/spaces
    fields = line.strip().split()
    if len(fields) < 16:
        raise ValueError(f"Expected >=16 fields in refGene line, got {len(fields)}: {line[:120]}...")
    bin_field, name, chrom, strand = fields[0], fields[1], fields[2], fields[3]
    txStart, txEnd = int(fields[4]), int(fields[5])
    cdsStart, cdsEnd = int(fields[6]), int(fields[7])
    exonCount = int(fields[8])
    exonStarts = [int(x) for x in fields[9].strip(",").split(",") if x]
    exonEnds = [int(x) for x in fields[10].strip(",").split(",") if x]
    score = fields[11]
    gene = fields[12]
    cdsStartStat, cdsEndStat = fields[13], fields[14]
    exonFrames = fields[15]
    if len(exonStarts) != exonCount or len(exonEnds) != exonCount:
        raise ValueError(
            f"Exon count mismatch for {name}: exonCount={exonCount}, starts={len(exonStarts)}, ends={len(exonEnds)}"
        )
    return {
        "name": name,
        "chrom": chrom,
        "strand": strand,
        "txStart": txStart,
        "txEnd": txEnd,
        "cdsStart": cdsStart,
        "cdsEnd": cdsEnd,
        "exonCount": exonCount,
        "exonStarts": exonStarts,
        "exonEnds": exonEnds,
        "gene": gene,
        "gene_id": bin_field,
    }


def clamp(value, lower, upper):
    return max(lower, min(upper, value))


def normalize_cds_padding(config):
    if not config:
        return None
    if not isinstance(config, dict):
        raise ValueError("padding.cds must be a mapping with 'upstream'/'downstream' integers")
    upstream = int(config.get("upstream", 0))
    downstream = int(config.get("downstream", 0))
    if upstream < 0 or downstream < 0:
        raise ValueError("CDS padding values must be >= 0")
    return {"upstream": upstream, "downstream": downstream}


def normalize_utr_inclusion(config):
    default = {"5UTR": True, "3UTR": True}
    if config is None:
        return default
    if not isinstance(config, dict):
        raise ValueError("segments.include_utrs must be a mapping")
    include = default.copy()
    if "five_prime" in config:
        include["5UTR"] = bool(config["five_prime"])
    if "three_prime" in config:
        include["3UTR"] = bool(config["three_prime"])
    return include


def apply_cds_padding(start, end, strand, cdsStart, cdsEnd, padding):
    if not padding:
        return start, end
    upstream = padding["upstream"]
    downstream = padding["downstream"]
    if strand == "-":
        upstream, downstream = downstream, upstream
    padded_start = clamp(start - upstream, cdsStart, cdsEnd)
    padded_end = clamp(end + downstream, cdsStart, cdsEnd)
    if padded_start >= padded_end:
        return start, end
    return padded_start, padded_end


def load_config(path, required=True):
    if not path:
        return {}
    if not os.path.exists(path):
        if required:
            raise FileNotFoundError(f"Config file '{path}' not found")
        return {}
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse config files. Please install it or remove --config.")
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError("Top-level config structure must be a mapping")
    return data


def exon_segments_with_labels(
    chrom,
    strand,
    gene,
    cdsStart,
    cdsEnd,
    exonStarts,
    exonEnds,
    order="transcript",
    cds_padding=None,
    metadata=None,
    include_utrs=None,
    is_noncoding=False,
):
    idxs = list(range(len(exonStarts)))
    if order == "transcript":
        if strand == "-":
            idxs = list(reversed(idxs))
    elif order == "genomic":
        pass
    else:
        raise ValueError("order must be 'transcript' or 'genomic'")

    include = include_utrs or {"5UTR": True, "3UTR": True}
    base_metadata = dict(metadata or {})

    def meta_for_exon(exon_number):
        meta = base_metadata.copy()
        meta["exon_number"] = exon_number
        return meta

    if is_noncoding:
        label = f"{gene}_ncRNA"
        for exon_number, exon_idx in enumerate(idxs, start=1):
            s = exonStarts[exon_idx]
            e = exonEnds[exon_idx]
            yield chrom, s, e, label, strand, meta_for_exon(exon_number)
        return

    def make_utr_label(position):
        """Return strand-aware UTR label for regions before/after the CDS."""
        if position not in {"before", "after"}:
            raise ValueError("position must be 'before' or 'after'")
        is_five_prime = (strand == "+" and position == "before") or (strand == "-" and position == "after")
        suffix = "5UTR" if is_five_prime else "3UTR"
        return f"{gene}_{suffix}"

    def allowed(label):
        if label.endswith("_5UTR"):
            return include.get("5UTR", True)
        if label.endswith("_3UTR"):
            return include.get("3UTR", True)
        return True

    for exon_number, exon_idx in enumerate(idxs, start=1):
        s = exonStarts[exon_idx]
        e = exonEnds[exon_idx]

        # Regions are named relative to transcript direction, not genomic coordinate
        if e <= cdsStart:
            label = make_utr_label("before")
            if allowed(label):
                yield chrom, s, e, label, strand, meta_for_exon(exon_number)
        # Completely after CDS
        elif s >= cdsEnd:
            label = make_utr_label("after")
            if allowed(label):
                yield chrom, s, e, label, strand, meta_for_exon(exon_number)
        # Crosses CDS start boundary: split into UTR then CDS
        elif s < cdsStart < e <= cdsEnd:
            label = make_utr_label("before")
            if allowed(label):
                yield chrom, s, cdsStart, label, strand, meta_for_exon(exon_number)
            yield chrom, *apply_cds_padding(cdsStart, e, strand, cdsStart, cdsEnd, cds_padding), f"{gene}_CDS", strand, meta_for_exon(exon_number)
        # Crosses CDS end boundary: split into CDS then UTR
        elif cdsStart <= s < cdsEnd < e:
            yield chrom, *apply_cds_padding(s, cdsEnd, strand, cdsStart, cdsEnd, cds_padding), f"{gene}_CDS", strand, meta_for_exon(exon_number)
            label = make_utr_label("after")
            if allowed(label):
                yield chrom, cdsEnd, e, label, strand, meta_for_exon(exon_number)
        # Fully within CDS
        elif s >= cdsStart and e <= cdsEnd:
            yield chrom, *apply_cds_padding(s, e, strand, cdsStart, cdsEnd, cds_padding), f"{gene}_CDS", strand, meta_for_exon(exon_number)
        else:
            # Handles rare edge-cases (e.g., non-canonical annotations)
            yield chrom, s, e, f"{gene}_unknown", strand, meta_for_exon(exon_number)


def get_bed_formatter(config, selected_name, split_utrs=True):
    if not selected_name:
        raise ValueError("A BED format name must be provided via --bed-format.")

    cfg = config or {}
    presets = cfg.get("bed_formats") or {}
    preset = presets.get(selected_name)
    if not preset:
        available = ", ".join(sorted(presets)) if presets else "none"
        raise ValueError(f"Unknown bed format '{selected_name}'. Available formats: {available}.")

    columns = preset.get("columns")
    if not columns:
        raise ValueError(f"bed_formats.{selected_name}.columns must be defined")
    templates = []
    for col in columns:
        if isinstance(col, dict):
            templates.append(str(col.get("value", "")))
        else:
            templates.append(str(col))

    def formatter(row):
        chrom, start, end, label, strand, meta = row
        meta = meta or {}
        base_gene = meta.get("gene", "")
        gene_for_output = base_gene
        if split_utrs and base_gene:
            if label.endswith("_5UTR"):
                gene_for_output = f"{base_gene}_5UTR"
            elif label.endswith("_3UTR"):
                gene_for_output = f"{base_gene}_3UTR"

        context = {
            "chrom": chrom,
            "start": start,
            "end": end,
            "label": label,
            "strand": strand,
            "gene": gene_for_output,
            "base_gene": base_gene,
            "transcript": meta.get("transcript", ""),
            "gene_id": meta.get("gene_id", ""),
            "exon_number": meta.get("exon_number", ""),
        }
        context["coords"] = f"{chrom}-{start}-{end}"
        try:
            columns_out = [template.format(**context) for template in templates]
        except KeyError as exc:
            raise ValueError(f"Unknown placeholder {exc} in bed_format columns") from exc
        return "\t".join(columns_out)

    return formatter


def write_bed(rows, out_path, formatter=None):
    with open(out_path, "w", encoding="utf-8") as out:
        for row in rows:
            if formatter:
                out.write(f"{formatter(row)}\n")
            else:
                chrom, s, e, label, strand, _meta = row
                out.write(f"{chrom}\t{s}\t{e}\t{label}\t0\t{strand}\n")


def write_query_metadata(out_path, config, bed_format_name):
    query_path = f"{os.path.splitext(out_path)[0]}_query.json"
    payload = {
        "config": config or {},
        "bed_format": bed_format_name,
    }
    with open(query_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)


def deduplicate_rows_by_coords(rows):
    seen = set()
    deduped = []
    for row in rows:
        chrom, start, end, *_rest = row
        key = (chrom, start, end)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    return deduped


def main():
    ap = argparse.ArgumentParser(
        description="Create BED of CDS/UTR segments for a given transcript from a refGene-like file."
    )
    ap.add_argument(
        "--refgene",
        required=True,
        help="Path to refGene file (optionally .gz) with at least 16 columns per UCSC refGene spec.",
    )
    ap.add_argument(
        "--transcript",
        dest="transcripts",
        nargs="+",
        help="One or more transcript identifiers (e.g., NM_001282225.2).",
    )
    ap.add_argument(
        "--transcript-file",
        help="Path to a text file containing one transcript ID per line (blank lines ignored).",
    )
    ap.add_argument("--out", required=True, help="Output BED file path.")
    ap.add_argument(
        "--config",
        help="Optional YAML config with padding settings (defaults to config.yaml next to this script if present).",
    )
    ap.add_argument(
        "--order",
        choices=["transcript", "genomic"],
        default="transcript",
        help="Order of BED rows. 'transcript' respects the transcript 5'->3' direction (reverse on - strand). Default: transcript.",
    )
    ap.add_argument(
        "--bed-format",
        dest="bed_format_name",
        required=True,
        help="Select the BED format preset defined in the config (e.g., sambamba, data).",
    )
    args = ap.parse_args()

    cli_transcripts = args.transcripts or []
    file_transcripts = []
    if args.transcript_file:
        if not os.path.exists(args.transcript_file):
            sys.stderr.write(f"ERROR: transcript file '{args.transcript_file}' not found.\n")
            sys.exit(1)
        with open(args.transcript_file, "r", encoding="utf-8") as tfh:
            for line in tfh:
                tid = line.strip()
                if tid:
                    file_transcripts.append(tid)

    transcripts = cli_transcripts + file_transcripts
    if not transcripts:
        sys.stderr.write("ERROR: Provide transcripts via --transcript or --transcript-file.\n")
        sys.exit(1)
    targets = {t: None for t in transcripts}
    missing = set(targets)

    with smart_open(args.refgene) as fh:
        for line in fh:
            if not line.strip() or line.startswith(("#", "track", "browser")):
                continue
            try:
                rec = parse_refgene_line(line)
            except Exception:
                continue
            name = rec["name"]
            if name in missing:
                targets[name] = rec
                missing.remove(name)
                if not missing:
                    break

    if missing:
        not_found = ", ".join(sorted(missing))
        sys.stderr.write(f"ERROR: Transcript(s) not found in {args.refgene}: {not_found}.\n")
        sys.exit(1)

    config_path = args.config
    if not config_path:
        default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")
        if os.path.exists(default_path):
            config_path = default_path

    config = load_config(config_path, required=False)
    cds_padding = normalize_cds_padding(config.get("padding", {}).get("cds"))
    segments_cfg = config.get("segments", {}) if isinstance(config, dict) else {}
    include_utrs = normalize_utr_inclusion(segments_cfg.get("include_utrs"))
    split_utrs = bool(segments_cfg.get("split_utrs", True))

    rows = []
    for transcript in transcripts:
        rec = targets[transcript]
        metadata = {"gene": rec["gene"], "transcript": rec["name"], "gene_id": rec.get("gene_id", "")}
        rows.extend(
            exon_segments_with_labels(
                chrom=rec["chrom"],
                strand=rec["strand"],
                gene=rec["gene"],
                cdsStart=rec["cdsStart"],
                cdsEnd=rec["cdsEnd"],
                exonStarts=rec["exonStarts"],
                exonEnds=rec["exonEnds"],
                order=args.order,
                cds_padding=cds_padding,
                metadata=metadata,
                include_utrs=include_utrs,
                is_noncoding=rec["name"].startswith("NR_"),
            )
        )

    rows.sort(key=lambda row: (row[0], row[1], row[2]))
    rows = deduplicate_rows_by_coords(rows)

    formatter = get_bed_formatter(config, selected_name=args.bed_format_name, split_utrs=split_utrs)
    write_bed(rows, args.out, formatter=formatter)
    write_query_metadata(args.out, config, args.bed_format_name)


if __name__ == "__main__":
    main()
