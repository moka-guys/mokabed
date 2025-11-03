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
Use Bedmaker to create bedfile for VCP1 and VCP2 genes with +/-30bp for variant calling and +/-10 for coverage.

Save Pan5294_VCP1_VCP2_transcripts.txt

Run bedmaker and save Pan5294_VCP1_VCP2_query.json

# Make VCP3/CP205 bedfile + non R code genes

Save Pan5294_VCP3_CP205_transcripts.txt and Pan5294_nonRcode_genes.txt

Bedmaker was unable to find any data for NM_001750.7 (CAST gene) in build 37 using the TARK API, therefore after an investigation by RLH it was proposed to use NM_001190442.1 and NM_001042440.2 for CAST.  Lu Liu approved the changes on 31/10/2025

Edit Pan5294_VCP3_CP205_transcripts.txt to replace CAST transcript NM_001750.7 with NM_001190442.1 and NM_001042440.2

Run bedmaker and save Pan5294_VCP3_CP2_nonRcode_query.json

# Make additional regions bedfile

Save CP205_pathogenicsnps_wrsids.txt, CP205_pathogenic_snps_norsids.txt and FXR1_noncoding_region.txt

Run bedmaker and save Pan5294_additionalregions_query.json

# Combine all bedfiles

cat Pan5294_VCP1_VCP2_data.bed Pan5294_additionalregions_data.bed >> Pan5294_VCP3_CP2_nonRcode_data.bed

# sort data.bed

sort Pan5294_VCP3_CP2_nonRcode_data.bed -k1,1V -k2,2n -k3,3n > Pan5294_VCP3_CP2_nonRcode_data_sorted.bed; mv Pan5294_VCP3_CP2_nonRcode_data.bed Pan5294_VCP3_CP2_nonRcode_unsorted_data.bed; mv Pan5294_VCP3_CP2_nonRcode_data_sorted.bed Pan5294_VCP3_CP2_nonRcode_data.bed; rm Pan5294_VCP3_CP2_nonRcode_unsorted_data.bed

Noticed a minor error in Pan5294_VCP3_CP2_nonRcode_data.bed, missed new line. 
1	25870076	25870277	26119	LDLRAP1;NM_015627.2, manually moved to the correct position 