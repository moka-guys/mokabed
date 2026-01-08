## Pan5304
CP205 CNV calling (R116) BED file (build37) for exomedepth CNV caller step.

## add request form
R116_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5UTR only. No padding. No additional regions requested.

## run refgene
refgene.py was run with R116_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R116/R116_transcripts.txt --bed-format cnv --out Pan5304_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing

generated bed was run with ED_cnv_calling_v1.6.0. The app completed without errors.