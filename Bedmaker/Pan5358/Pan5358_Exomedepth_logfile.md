## Pan5358
This Pan number is to be used for 
 - Readcount/ExomeDepth Bed file (CNV whole capture bed) for CNV calling 

This is to replace the existing bed (Pan5356_exomeDepth.bed) that has typo in GREM1_SCG5_4. The two genes should be separated with dash (-), not with underscore (_).

## Copy Pan5356 to Pan5358 ExomeDepth bed
cp Pan5356/Pan5356_exomeDepth.bed Pan5358/

## Correcting typo
15	32996308	32996427	GREM1_SCG5_4  is updated to 15	32996308	32996427	GREM1-SCG5_4


## rename bed file
The bed file was renamed as Pan5358
mv Pan5356_exomeDepth.bed Pan5358_exomeDepth.bed

## testing
The updated readcount bed was tested using ED_readcount_analysis_v1.6.1. The expected readcount RData is generated