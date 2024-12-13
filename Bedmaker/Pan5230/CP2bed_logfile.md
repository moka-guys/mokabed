## Pan5230
CP2 Whole Capture BED file (build37) for coverage and variant calling

To include:
- Genes that are included in R code tests that will be tested on CP2, provided as a transcript ID with a version (see text file XXX)
- Genes that are not included on R code tests at the moment, provided as gene name. BEDmaker will select the MANE transcript equivalent or the Ensembl canonical transcript if the MANE equivalent is unavailable. (File XXX)
- SNPs (for FH PRS and know pathogenic SNPs in other regions) Provided as a list of rsIDs (CP2_pathogenicsnps_wrsids.txt)
- Genomic regions (some SNPs, some known clinically important non-coding regions) provided as a list of regions (CP2_pathogenic_snps_norsids.txt padded by +/-5bp)

5'UTR included for all genes, padded by +/-30bp

Padding:
Padding for data.bed- exons +/-30bp
Padding for sambamba.bed- exons +/-10bp
SNPs (when rsID provided) padded +/-5bb for all files


Lists produced by R Haines and N Pinto using information from Heidi and Michael. 

Lists reviewed by XXX prior to Bed file being used
Date: