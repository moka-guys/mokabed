Pan4909 contains all the FH SNPs without any padding.

The bedfile is based on Pan4909 which contains only the intronic variants.

## Get copy of Pan4292
cp Pan4292.bed Pan4909.bed

## Manually remove padding
All SNPs in Pan4909 are padded by +-5bp
Padding was removed in Excel

## Add additional FH SNPs
2:21263900 19:45411941 19:45412079

## Sort Pan4909.bed
sort Pan4909.bed -k1,1V -k2,2n -k3,3n > Pan4909_sorted.bed

## Rename BEDfile
mv Pan4909_sorted.bed Pan4909.bed

## Re-sort the BEDfike
During testing it was noticed the chr number and start position were combined in the second column:
correct: 
1	55504649

incorrect
155504649

This was corrected and the BED file was re-sorted
sort Pan4909.bed -k1,1V -k2,2n -k3,3n > Pan4909_sorted.bed

#Rename BEDfile
mv Pan4909_sorted.bed Pan4909.bed

## Testing statement
The BEDfile has been tested in 003_210707_FH_app. It completed without errors and returned expected outputs.