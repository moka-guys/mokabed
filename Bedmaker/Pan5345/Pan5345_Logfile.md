## Pan5345
CP205 CNV calling (R424) BED file (build37) for exomedepth CNV caller step.

## add request form
R424_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions added.

## run refgene
refgene.py was run with R424_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R424/R424_transcripts.txt --bed-format cnv --out Pan5345_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
generated bed was tested with ED_cnv_calling_v1.6.0. The app completed without errors.