## Pan5346
CP205 Whole Capture BED file (build37) for coverage and variant calling

This BEDfile replaces Pan5294; during validation, coverage issues were spotted with single exons genes containing the 5' and 3' UTRs, therefore BEDfiles need to be remade.

# Copy Pan5294 bedfiles
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_data.bed Pan5346_data.bed
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_sambamba.bed Pan5346_sambamba.bed

# Update BEDfiles
List of single exon genes with 5UTR and 3UTR included curated by George Doyle and Rebecca Haines.
5UTR and 3UTR regions trimmed from VCP3/CP2 genes and 5UTR retained for the VCP2 gene (GREM1), see trimmed_singleexon_regions.txt (not padded) for full list

# Manually fix trimmed regions in data.bed
Use VScode to update Pan5346_data.bed with trimmed regions

Padding info:
- All VCP3/CP2 trimmed regions were padded +/10bp
- VCP2 gene (GREM1, GREM1_5UTR) was padded +/-30bp

# Repeat for coverage bedfile
Use VScode to update Pan5346_sambamba.bed with trimmed regions

Padding info:
- All VCP3/CP2 trimmed regions were padded +/10bp
- VCP2 gene (GREM1, GREM1_5UTR) was padded +/-10bp

# Testing 
Pan5346_data.bed was tested in DNAnexus using Moka Picard v1.2. The app completed successfully without any errors.

Pan5346_sambamba.bed was tested using sambamba_coverage_v2.0.3 The app completed successfully without any errors.

# Remove GREM UTR padding
GREM1 5UTR 15:33022890-33022891 was accidentally padded. 
Padding for the 5UTR removed from Pan5346_data.bed and Pan5346_sambamba.bed to be consistent with the other UTRs in the bedfiles.

# Testing 
Pan5346_data.bed was tested in DNAnexus using Moka Picard v1.2. The app completed successfully without any errors.

Pan5346_sambamba.bed was tested using sambamba_coverage_v2.0.3 The app completed successfully without any errors.

## Manual adjustments to KCNA1 gene to trimming 3' UTR, include padding - 05/01/2026
Updates to Pan5346_data.bed and Pan5346_sambamba.bed in order to correct single exon gene issue (Requires 3' UTR removal and padding +10).

## Ran refgene.py using single NM_000217.3 transcript for updating data.bed file
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file KCNA1.txt --bed-format data --out KCNA1.bed --config config.yaml

KCNA1_query_json:

{
  "bed_format": "data",
  "config": {
    "bed_formats": {
      "cnv": {
        "columns": [
          "{chrom}",
          "{start}",
          "{end}",
          "{gene};{transcript}"
        ],
        "strip_chr_prefix": true
      },
      "data": {
        "columns": [
          "{chrom}",
          "{start}",
          "{end}",
          "{gene_id}",
          "{gene};{transcript}"
        ],
        "strip_chr_prefix": true
      },
      "exomedepth": {
        "columns": [
          "{chrom}",
          "{start}",
          "{end}",
          "{gene}_{exon_number}"
        ]
      },
      "sambamba": {
        "columns": [
          "{chrom}",
          "{start}",
          "{end}",
          "{coords}",
          "0",
          "{strand}",
          "{gene};{transcript}",
          "{gene_id}"
        ]
      }
    },
    "padding": {
      "cds": {
        "downstream": 0,
        "upstream": 0
      }
    },
    "segments": {
      "include_utrs": {
        "five_prime": true,
        "three_prime": false
      },
      "split_utrs": true
    }
  }
}

* Note that padding is not applied as current refgene.py logic will not extend CDS into UTR regions. This will have to be updated manually.