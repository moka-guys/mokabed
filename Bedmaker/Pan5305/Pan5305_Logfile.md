## Pan5305
CP205 CNV calling (R117) BED file (build37) for exomedepth CNV caller step.

# add request form
R117_BEDfile_request_form.csv is added into LiveBedfiles/RequestForms
5' UTR only, no padding, no additional regions

# run refgene
rungene.py was run with R117_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R117/R117_transcripts.txt --bed-format cnv --out Pan5305_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml