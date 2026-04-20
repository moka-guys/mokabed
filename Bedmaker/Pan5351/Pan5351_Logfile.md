## Pan5351
CP205 CNV calling (R210) BED file (build37) for exomedepth CNV caller step.

## Copy Pan5318 CNV bed to Pan5351 CNV bed
Pan5318_CNV.bed is existing bed file for R210. For additional changes, R5318_CNV.bed was copied into Pan5351_CNV.bed


cp ../Pan5318/Pan5318_CNV.bed ./Pan5351_CNV.bed

## run bedmaker
NM_207421.3 was used for PADI6 gene to run bedmaker
## combine bed files
cat Pan5351_cnv_PADI6.bed >> Pan5351_CNV.bed

## sorting
sort -k1,1V -k2,2n Pan5351_CNV.bed -o Pan5351_CNV.bed


