## Pan5275

CP2v2 Whole Capture BED file (build37) for coverage and variant calling.

Some additional genes were requested in CPv2, the additional genes and transcripts were provided by Heidi K.

Files used to create the original CP2 variant calling bedfiles (Pan5230 and Pan5232) were re-used to for Pan5275, however Pan5232_CP2_transcripts.txt was updated to include the new genes.


# Files used to create Pan5275
- Genes that are included in R code tests that will be tested on CP2v2, including the newly requested genes, provided as a transcript ID with a version (see text file Pan5275_CP2_transcripts.txt)
- Genes that are not included on R code tests at the moment, provided as gene name. BEDmaker will select the MANE transcript equivalent or the Ensembl canonical transcript if the MANE equivalent is unavailable. (Pan5230_CP2_nonRgenes.txt)
- SNPs (for FH PRS and know pathogenic SNPs in other regions) Provided as a list of rsIDs (Pan5230_CP2_pathogenicsnps_wrsids.txt)
- Genomic regions (some SNPs, some known clinically important non-coding regions) provided as a list of regions
(Pan5230_CP2_pathogenic_snps_norsids.txt padded by +/-5bp)
- FXR1 non-coding region will be padded by +/-30bp, provided in Pan5230_FXR1_noncoding_region.txt. This region is for the muscle specific transcript described in https://doi.org/10.1038/s41467-019-08548-9

5'UTR included for all genes, padded by +/-30bp


# Copy Pan5232_CP2_transcripts.txt

cp Pan5232_CP2_transcripts.txt Pan5275_CP2_transcripts.txt

# Add new transcripts provided by Heidi

Seven new genes transcript (wiht versions) were added to Pan5275_CP2_transcripts.txt

