## Pan5350
CP205 CNV calling (R208) BED file (build37) for exomedepth CNV caller step.

## Copy Pan5317_CNV bed to Pan5350 CNV bed
Pan5317_CNV.bed is existing bed file for R208. For additional changes, Pan5317_CNV.bed file was copied as Pan5350_CNV.bed
cp ../Pan5317/Pan5317_CNV.bed ./Pan5350_CNV.bed

## Run bedmaker
NM_000465.2 is used for BARD1 gene to run bedmaker. 

## combine bed files
cat Pan5350_cnv_BARD1.bed >> Pan5350_CNV.bed 

## sorting
sort -k1,1V -k2,2n Pan5350_CNV.bed -o Pan5350_CNV.bed
## testing
generated bed file was tested with ED_cnv_calling_v1.7.0 and the app finished without error. 