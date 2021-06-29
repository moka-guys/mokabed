# Pan4398 Exomedepth
This BED file is used for Exomedepth on VCP1 panel.
It contains the numbered and unpadded meta-exons. Meta-exons are built from the overlap of exons with the capture regions and collapsed to build a virtual transcript that contains all exons of the collapsed transcripts. Exons numbers are not necessarily congruent withthe exon number of a given transcript and a caveat will be added to the exomedepth report.

Analogous to the patches applied to the other BED files of the panel (eg. see Pan4362_logfile.md), additional exoms must be added to ensure the mapped refseq transcripts are congruent with the capture regions. The added regions (exons) are stored in Pan4398_extra.bed.

## Process to build exomdepth capture file

1. Convert the capture BED to BED4 format `cut -f1-4 Pan4398data.bed > Pan4389capture.bed`

2. Run the makeExomedepth script to identify capture regions not part of the UCSC RefGene Set:

 	`./makeExomedepth.sh hg19 tmp Pan4398capture.bed`

3. Edit `tmp_missed.bed` to use gene symbol as BED4 column, and rename to `Pan4398_extra.bed`

4. Run makeExomedepth to generate final exomdepth BED file (Pan4398_exomdepth.bed)

`./makeExomedepth.sh hg19 Pan4398final Pan4398capture.bed Pan4362_extra.bed`
                     |    |            |                  |
                     |    |            |                  +- additional exons (not included in UCSC dataset)
                     |    |            +- the capture (BED4 format)
                     |    +- output file name root
                     +- the ucsc database (assembly) to use for annotation retrieval

5. Ensure no regions are reported as missed and `Pan4398final_missed.bed` is empty.

6. Final exomedepth BED file is written as `Pan4398final_exomedepth.bed` renamed to `Pan4398exomedepth.bed`
