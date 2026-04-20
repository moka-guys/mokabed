## Pan5352
CP205 CNV calling (R211) BED file (build37) for exomedepth CNV caller step.

## Copy Pan5320_CNV bed to Pan5352 CNV bed
Pan5320_CNV.bed is existing bed file for R211. For additional changes, Pan5320_CNV.bed file was copied as Pan5352_CNV.bed

cp ../Pan5320/Pan5320_CNV.bed ./Pan5352_CNV.bed

## Run bedmaker
NM_001276270.1 is used for MBD4 gene to run bedmaker

## combine bed files
cat Pan5352_cnv_MBD4.bed >> Pan5352_CNV.bed
## sorting
sort -k1,1V -k2,2n Pan5352_CNV.bed -o Pan5352_CNV.bed

