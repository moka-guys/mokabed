## Pan5300
CP205 CNV calling (R25) BED file (build37) for exomedepth CNV caller step.

## add request form
R25_BEDfile_request_form.csv was added into /LiveBedfiles/RequestForms
5 UTR only. No padding. No additional regions requested.

## run bedmaker
bedmaker was run for NM_000142.4 as it is not in ncbiRefSeq.txt

## testing
generated bed was run with ED_cnv_calling_v1.6.0. The app completed without error