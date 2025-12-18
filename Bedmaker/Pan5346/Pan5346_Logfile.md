## Pan5346
CP205 Whole Capture BED file (build37) for coverage and variant calling

This BEDfile replaces Pan5294; during validation, coverage issues were spotted with single exons genes containing the 5' and 3' UTRs, therefore BEDfiles need to be remade.

# Copy Pan5294 bedfiles
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_data.bed Pan5346_data.bed
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_sambamba.bed Pan5346_sambamba.bed

# Update BEDfiles
List of single exon genes with 5UTR and 3UTR included curated by George Doyle.
5UTR and 3UTR regions trimmed from VCP3/CP2 genes and 5UTR retained for the VCP2 gene (GREM1), see trimmed_singleexon_regions.txt for full list

# Manually fix trimmed regions
Use VScode to update Pan5346_data.bed with trimmed regions

Since GREM1 is a VCP2 gene, we need to retain 5UTR region, however it was noticed the 5UTR was not split from the exon in trimmed_singleexon_regions.txt

trimmed_singleexon_regions.txt was updated to split the exon and the 5UTR (only 1bp)
Pan5346_data.bed updated to include the GREM1 regions

Note: no padding was added to these regions as this would lead to UTRs being included.

# Repeat for coverage bedfile
Use VScode to update Pan5346_sambamba.bed with trimmed regions


# Testing 
Pan5346_data.bed was tested in DNAnexus using Moka Picard v1.2. The app completed successfully without any errors.

Pan5346_sambamba.bed was tested using sambamba_coverage_v2.0.3 The app completed successfully without any errors.