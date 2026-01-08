## Pan5312
CP205 CNV calling (R124) BED file (build37) for exomedepth CNV caller step.

## add request form
R124_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5 UTR only. No padding. No additional regions requested.

## run refgene
refgene.py was run with R124_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R124/R124_transcripts.txt --bed-format cnv --out Pan5312_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
generated bed was tested with ED_cnv_calling_v1.6.0. The app completed without error.