# Pan5325
CP205 CNV calling (R444.1) BED file (build37) for exomedepth CNV caller step.

## Save request form
Pan5325_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. 3UTR included as an additional region for BRCA1, BRCA2 and PALB2. 8 additional regions also included for BRCA1 (BRCA1_IN11_1,BRCA1_IN11_2,BRCA1_IN12_1,BRCA1_IN12_2,BRCA1_PM_5_1,BRCA1_PM_5_2,BRCA1_PM_5_3,BRCA1_PM_5_4).

## Run refgene.py
Use Pan5325_transcript.txt to run refgene.py
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file Pan5325_transcript.txt --bed-format cnv --out Pan5325_CNV.bed