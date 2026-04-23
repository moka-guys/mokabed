## Pan5356
This Pannumber is used for small variant calling/filtering bed file (i.e. data.bed)

## Copy Pan5347 to Pan5356
Existing small variant calling/filtering bed file is Pan5347_data.bed. To make additional changes, Pan5347 was copied into Pan5356

cp ../Pan5347/Pan5347_data.bed ./Pan5356_data.bed

## Extend the padding region 
BARD1 and MBD4 genes were added into CNV calling bed files for R208 and R211 respectively, that are VCP2 panels. For VCP2, +/-30 padding is needed, so for these genes, additional +/-20 padding was added manually