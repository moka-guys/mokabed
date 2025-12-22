## Pan5346
CP205 Whole Capture BED file (build37) for coverage and variant calling

This BEDfile replaces Pan5294; during validation, coverage issues were spotted with single exons genes containing the 5' and 3' UTRs, therefore BEDfiles need to be remade.

# Copy Pan5294 bedfiles
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_data.bed Pan5346_data.bed
cp /home/natashapinto/Documents/mokabed/Bedmaker/Pan5294/Pan5294_sambamba.bed Pan5346_sambamba.bed