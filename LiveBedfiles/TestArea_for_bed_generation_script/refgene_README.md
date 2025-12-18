# ncbiRefSeq_bedgen

Utility scripts for:

- Producing BED files from the UCSC ncbiRefSeq.txt files used for IGV transcript annotation.
- Checking that list of transcripts is present within a given BED file.

## Generate BED files

```
python3 refgene.py \
  --refgene ncbiRefSeq.txt \
  --transcript-file transcripts.txt \
  --out out.bed \
  --config config.yaml \
  --bed-format sambamba
```

Key options:
- `--transcript` / `--transcript-file` supply one or more target IDs (e.g. NM_001282225.2 or .txt file containing line separated identifiers).
- `--bed-format` (required) selects one of the presets defined under `bed_formats` in `config.yaml` (`sambamba`, `data`, `exomedepth`, `cnv` , …).
- `--order` controls row ordering (`transcript` keeps biological direction; `genomic` sorts by coordinate).

`config.yaml` also drives CDS padding (`padding.cds`), UTR inclusion (`segments.include_utrs`), UTR naming (`segments.split_utrs`), and houses the reusable BED format presets under `bed_formats`.

Every run also writes a companion JSON file next to the BED (e.g., `out_query.json`) that captures the config settings and selected format for traceability.

## Validate coverage

```
python3 check_transcripts.py \
  --transcripts transcripts.txt \
  --bed out.bed
```

This verifies every requested transcript identifier appears in the BED output (based on the final column schema).
