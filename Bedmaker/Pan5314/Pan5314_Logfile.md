## Pan5314
CP205 CNV calling (R184) BED file (build37) for exomedepth CNV caller step

## add request form
R184_BEDfile_request_form.csv is added into LiveBedfiles/RequestForms
5' UTR, no padding. No additional regions requested.

## run refgene
refgene was run with R184_transcripts.txt 

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R184/R184_transcripts.txt --bed-format cnv --out Pan5314_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml