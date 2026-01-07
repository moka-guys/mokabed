# Pan5340
CP205 CNV calling (R236) BED file (build37) for exomedepth CNV caller step.

## Save request form
Pan5340_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

No padding. Multiple transcripts requested for genes BRAF, CDKN2A, HRAS, KRAS, MITF, PSENEN, SOS1, WRAP53, and LMNA. 21 additional regions requested. 

## Run refgene.py
Manually created Pan5340_transcripts_ncbi.txt from the Request form, and used as the input to run refgene.py

```
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file ../../Bedmaker/Pan5340/Pan5340_transcripts_ncbi.txt --bed-format cnv --out Pan5340_CNV.bed
```

## Run bedmaker for ENST transcripts and additional regions
Requested to add 21 additional regions, and 3 Ensembl transcripts. 
Ran BEDmaker (:8080) using settings to split UTRs, NOT include 5'UTR, and NOT include 3'UTR.
Saved outputs.

## Edit additional BED labels
Removed duplicate regions and updated labels in Pan5340_cnv_additional_regions.bed to match request form.

## Combine BED files
```
cat Pan5340_cnv_additional_regions.bed >> Pan5340_CNV.bed 
```

## Sort Pan5340_CNV.bed
```
sort -k1,1V -k2,2n Pan5340_CNV.bed -o Pan5340_CNV.bed
```