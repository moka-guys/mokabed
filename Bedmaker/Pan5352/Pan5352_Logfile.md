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

## testing
updated Bed file was tested with ED_cnv_calling_v1.7.0 and the app finished without error.

## add request form
R211_BEDfile_request_form_april2026.csv was added into mokabed/LiveBedfiles. In the request form the newly added transcript for MBD4 is NM_001276270.2. However, NM_001276270.1 was used as this is the transcript used in small variant capture bed (i.d. data.bed). Both transcript have the same CCDS number CCDS63768.1"

## split 5UTR
It was noted that 5UTR was missed to split from  exon. The UTR region was split manually.

## testing 
Amended bed file was tested again ED_cnv_calling_v1.7.0 and the app finished without error.