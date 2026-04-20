## Pan5355
CP205 CNV calling (R81) BED file (build37) for exomedepth CNV caller step.

## Copy Pan5329 to Pan5355
Pan5329_CNV.bed was existing bed file for R81. For additional changes, Pan5329 was copied into Pan5355_CNV.bed

cp ../Pan5329/Pan5329_CNV.bed ./Pan5355_CNV.bed

## run bed maker
NM_004804.2 and NM_002916.3 were used to run CIAO1 and RFC4 gene respectively (No 5UTR)
## combine bed files
cat Pan5355_cnv_CIAO1_RFC4.bed >> Pan5355_CNV.bed
## sorting
sort -k1,1V -k2,2n Pan5355_CNV.bed -o Pan5355_CNV.bed

## testing
Bed file was tested using ED_cnv_caller_v1.7.0 and the app finished without error