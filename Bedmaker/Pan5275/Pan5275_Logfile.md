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

Padding:
Padding for data.bed- exons +/-30bp
Padding for sambamba.bed- exons +/-10bp
SNPs (when rsID provided) padded +/-5bb for all files


# Copy Pan5232_CP2_transcripts.txt

cp Pan5232_CP2_transcripts.txt Pan5275_CP2_transcripts.txt

# Add new transcripts provided by Heidi

Seven new genes transcript (wiht versions) were added to Pan5275_CP2_transcripts.txt

# Run Bedmaker
Pan5275_bedfile_query.json contains the original query given to bedmaker to generate the bedfiles.

# Check for formatting errors
data.bed and sambamba.bed were checked for gene naming issues fixed in Pan5272

Both bedfiles did not have any naming errors.

# Testing 
Pan5275_data.bed was tested in DNAnexus using Moka Picard v1.2. The app completed successfully without any errors.

Pan5275_sambamba.bed was tested using sambamba and chanjo v1.13. The app completed successfully without any errors.

# Add exon 1 of DMD (NM_000109.4)

We currently use NM_004006.2 for DMD, however we have been requested to add exon 1(NM_000109.4)

Rebecca Haines used UCSC and IGV to obtain the exon 1 coordinates (chrX:33357376-33357505), these were manually added to the data.bed and sambamba.bed 

The exon was padded by +/-30bp to be consistent with the rest of the regions in the bedfiles.

Region added chrX:33357346-33357535

This was repeated for sambamba.bed but the region has been padded by +/-10bp

Region added chrX:33357366-33357515

# Sort bedfiles

Data.bed and sambamba were sorted to ensure the region is placed 

sort Pan5275_data.bed -k1,1V -k2,2n -k3,3n > Pan5275_sorted.bed;mv Pan5275_data.bed Pan5275_unsorted.bed; mv Pan5275_sorted.bed Pan5275_data.bed; rm Pan5275_unsorted.bed

sort Pan5275_sambamba.bed -k1,1V -k2,2n -k3,3n > Pan5275sambamba_sorted.bed;mv Pan5275_sambamba.bed Pan5275sambamba_unsorted.bed; mv Pan5275sambamba_sorted.bed Pan5275_sambamba.bed; rm Pan5275sambamba_unsorted.bed
