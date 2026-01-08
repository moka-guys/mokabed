## Pan5306
CP205 CNV calling (R118) BED file (build37) for exomedepth CNV caller step.

## add request form
R118_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5 UTR added. No padding. No additional region requested.

## run refgene
refgene.py was run with R118_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R118/R118_transcripts.txt --bed-format cnv --out Pan5306_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml