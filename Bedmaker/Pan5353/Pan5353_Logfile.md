## Pan5353
CP205 CNV calling bed file for R79 to be used with Exomedepth

## Copy Pan5328 to Pan5353
Pan5328_CNV.bed was existing bed file for R79. For additional changes, Pan5328 was copied into Pan5353.

cp ../Pan5328/Pan5328_CNV.bed ./Pan5353_CNV.bed

## run bedmaker
NM_004804.2 was used to run bedmaker for CIAO1 gene (no UTR)
## combine bed files
cat Pan5353_CIAO1_cnv.bed >> Pan5353_CNV.bed
## sorting
sort -k1,1V -k2,2n Pan5353_CNV.bed -o Pan5353_CNV.bed

## testing
Bed file was tested using ED_cnv_calling_v1.7.0 and the app finished without error.

## add request form 
R79_BEDfile_request_form_april2026.csv was added into mokabed/LiveBedfiles
In the request form the newly added transcript for CIAO1 is NM_004804.3. However, NM_004804.2 was used as this is the transcript used in small variant capture bed (i.d. data.bed). Both transcript have the same CCDS number CCDS2019.1
                                                                               