## Pan5307
CP205 CNV calling (R119) BED file (build37) for exomedepth CNV caller step.

## add request form
R119_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms.
5 UTR, no padding. No additional region requested.

## run refgene
refgene.py was run with R119_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R119/R119_transcripts.txt --bed-format cnv --out Pan5307_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
generated bed file was run with ED_cnv_calling_v1.6.0. The app completed without error