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
