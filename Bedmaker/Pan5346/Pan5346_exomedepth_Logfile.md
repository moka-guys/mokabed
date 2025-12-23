## Pan5346_exomedepth
CP205 Whole Capture BED file (build37) for CNV calling (readcount) using Exomedepth

This BEDfile replaces Pan5294; during validation, coverage issues were spotted with single exons genes containing the 5' and 3' UTRs, therefore BEDfiles need to be remade.

# Copy Pan5294 bedfiles
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_exomeDepth.bed Pan5346_exomeDepth.bed

# Manually fix trimmed regions in data.bed
Use VScode to update Pan5346_exomeDepth.bed with trimmed regions (trimmed_singleexon_regions.txt)

# Testing
Pan5346_exomeDepth.bed was tested in DNAnexus using ED_readcount_analysis_v1.5.0 and ED_cnv_calling_v1.4.0. The apps completed successfully without any errors.

# move GREM1 UTR
GREM1 5UTR was in the correct order, it was manually moved.

