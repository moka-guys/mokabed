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

## adding the request form
R208_BEDfile_request_form_april2026.csv was added into mokabed/LiveBedfiles/
In the request form the newly added transcript for BARD1 is NM_000465.4. However, NM_000465.2 was used as this is the transcript used in small variant capture bed (i.d. data.bed). Both transcript have the same CCDS number CCDS2397.1

## split 5UTR
5UTR region for BARD1 was missed to split. It was split manually

