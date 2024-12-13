## Pan5230
CP2 Whole Capture BED file (build37) for coverage and variant calling

To include:
- Genes that are included in R code tests that will be tested on CP2, provided as a transcript ID with a version (see text file CP2_transcripts.txt)
- Genes that are not included on R code tests at the moment, provided as gene name. BEDmaker will select the MANE transcript equivalent or the Ensembl canonical transcript if the MANE equivalent is unavailable. (CP2_nonRgenes.txt)
- SNPs (for FH PRS and know pathogenic SNPs in other regions) Provided as a list of rsIDs (CP2_pathogenicsnps_wrsids.txt)
- Genomic regions (some SNPs, some known clinically important non-coding regions) provided as a list of regions
(CP2_pathogenic_snps_norsids.txt padded by +/-5bp)
- FXR1 non-coding region will be padded by +/-30bp, provided in FXR1_noncoding_region.txt. This region is for the muscle specific transcript described in https://doi.org/10.1038/s41467-019-08548-9

5'UTR included for all genes, padded by +/-30bp

Padding:
Padding for data.bed- exons +/-30bp
Padding for sambamba.bed- exons +/-10bp
SNPs (when rsID provided) padded +/-5bb for all files


Lists produced by R Haines and N Pinto using information from Heidi and Michael. 

# Pan5230_bedfile_query.json

Pan5230_bedfile_query.json contains the original query given to bedmaker to generate the bedfiles.


# Testing done in 003_241223_Pan5230bedfile
Pan5230_data.bed was tested in DNAnexus using Moka Picard v1.2. The app completed successfully without any errors.

Pan5230_sambamba.bed was tested using sambamba and chanjo v1.13. The app completed successfully without any errors.
