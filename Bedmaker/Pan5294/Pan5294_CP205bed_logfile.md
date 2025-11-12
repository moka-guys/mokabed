## Pan5294
CP205 Whole Capture BED file (build37) for coverage and variant calling

The bedfile consists of 

- VCP1 and VCP2 genes- to be padded +/-30bp for variant calling (+/-10 for coverage)
- VCP3/CP205 genes + non R code genes- to be padded +/- 10bp for variant calling and coverage
- SNPs (for FH PRS and know pathogenic SNPs in other regions) Provided as a list of rsIDs (CP205_pathogenicsnps_wrsids.txt)
- Genomic regions (some SNPs, some known clinically important non-coding regions) provided as a list of regions (CP205_pathogenic_snps_norsids.txt padded by +/-5bp)
- FXR1 non-coding region will be padded by +/-30bp, provided in FXR1_noncoding_region.txt. This region is for the muscle specific transcript described in https://doi.org/10.1038/s41467-019-08548-9

5'UTR included for VCP1 and VCP2 genes only; no padding

Lists produced by R Haines and N Pinto using information from Heidi and Michael. 

# Make VCP1 and VCP2 genes bedfile
Save Pan5294_VCP1_VCP2_transcripts.txt

# Save script used to generate bedfiles
Save refgene.py, refgene_readme.md, check_transcript.py, config.yaml and ncbiRefSeq.txt 

# Run refgene.py
Run refgene.py to create bedfiles for VCP1 and VCP2 genes with +/-30bp for variant calling and +/-10 for coverage.

# Make VCP3/CP205 bedfile + non R code genes
Save Pan5294_VCP3_CP205_transcripts.txt and Pan5294_nonRcode_genes.txt