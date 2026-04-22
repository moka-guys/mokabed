## Pan5356
This Pan number is to be used for 
 - Readcount/ExomeDepth Bed file (CNV whole capture bed) for CNV calling 

## Copy Pan5346 to Pan5356 ExomeDepth bed
Pan5346 is existing Readcount/Exomedepth whole capture bed. For additional changes, Pan5346 was copied into Pan5356

cp ../Pan5346/Pan5346_exomeDepth.bed ./Pan5356_exomeDepth.bed

## Adding 5UTR regions
BARD1 and MBD4 gene were added into R208 and R211 CNV bed files. These panels are VCP2 panel, therefore 5UTR regions were included in the CNV bed. To match CNV bed and readcount bed file, 5UTR regions were added for these genes. 
5' UTR regions for these genes were obtained from Pan5350_CNV.bed and Pan5352_CNV.bed respectively. 