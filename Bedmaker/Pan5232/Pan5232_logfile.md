## Pan5232

CP2 Whole Capture BED file (build37) for coverage and variant calling.
There was an issue with the original CP2 bedfile Pan5230, so the bedfile had to be remade. The incorrect transcript was provided for the gene ABHD5, in Pan5232 the transcript was corrected to NM_016006.4 from NM_020676.5 (ABHD6 transcript). The correct transcript was provided by Heidi K.

# Files included
- Genes that are included in R code tests that will be tested on CP2, provided as a transcript ID with a version (see text file Pan5232_CP2_transcripts.txt)
- Genes that are not included on R code tests at the moment, provided as gene name. BEDmaker will select the MANE transcript equivalent or the Ensembl canonical transcript if the MANE equivalent is unavailable. (Pan5230_CP2_nonRgenes.txt)
- SNPs (for FH PRS and know pathogenic SNPs in other regions) Provided as a list of rsIDs (Pan5230_CP2_pathogenicsnps_wrsids.txt)
- Genomic regions (some SNPs, some known clinically important non-coding regions) provided as a list of regions
(Pan5230_CP2_pathogenic_snps_norsids.txt padded by +/-5bp)
- FXR1 non-coding region will be padded by +/-30bp, provided in Pan5230_FXR1_noncoding_region.txt. This region is for the muscle specific transcript described in https://doi.org/10.1038/s41467-019-08548-9

5'UTR included for all genes, padded by +/-30bp

Padding:
Padding for data.bed- exons +/-30bp
Padding for sambamba.bed- exons +/-10bp
SNPs (when rsID provided) padded +/-5bb for all files

Lists produced by R Haines and N Pinto using information from Heidi and Michael. 

# Fix ABHD5
cp Pan5230_CP2_transcripts.txt ../Pan5232/Pan5232_CP2_transcripts.txt

Manually fix Pan5232_CP2_transcripts.txt by using the find and replace function in VScode.
Transcript changed from NM_020676.5 to NM_016006.4

# Run Bedmaker
Pan5232_bedfile_query.json contains the original query given to bedmaker to generate the bedfiles.