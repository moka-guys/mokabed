## Pan5302
CP205 CNV calling (R112) BED file (build37) for exomedepth CNV caller step.

## add request form
R112_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5UTR added. No padding. No additional region request

## run refgene
refgene.py was added with R112_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R112/R112_transcripts.txt --bed-format cnv --out Pan5302_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml