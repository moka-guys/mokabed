## Pan5318
CP205 CNV calling (R210) BED file (build37) for exomedepth CNV caller step.

## add request form
R210_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5' UTR only, no padding. Additional regions are requested.

## run refgene
refgene.py was run with R210_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R210/R210_transcripts.txt --bed-format cnv --out Pan5318_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions