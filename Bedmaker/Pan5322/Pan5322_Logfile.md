## Pan5322
CP205 CNV calling (R259) BED file (build37) for exomedepth CNV caller step.

## add request from
R259_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5 UTR only, no padding. No additional regions.

## run refgene
refgene was run with R259_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R259/R259_transcripts.txt --bed-format cnv --out Pan5322_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml