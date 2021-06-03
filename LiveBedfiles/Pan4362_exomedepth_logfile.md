# Pan4362 Exomedepth
This BED file is used for Exomedepth on VCP3 panel.
It contains the numbered and unpadded meta-exons. Meta-exons are built from the overlap of exons with the capture regions and collapsed to build a virtual transcript that contains all exons of the collapsed transcripts. Exons numbers are not necessarily congruent withthe exon number of a given transcript and a caveat will be added to the exomedepth report.

Analogous to the patches applied to the other BED files of the panel (see Pan4362_logfile.md), additional exoms must be added to ensure the mapped refseq transcripts are congruent with the capture regions. The added regions (exons) are stored in Pan4632_extra.bed.

# Generating the BED file for Exomedepth
./makeExomedepth.sh hg19 output Pan4361.bed Pan4362_extra.bed
                    |    |      |           |
                    |    |      |           +- additional exons (not included in UCSC dataset)
                    |    |      +- the capture (BED4 format)
                    |    +- output file name root
                    +- the ucsc database (assembly) to use for annotation retrieval

