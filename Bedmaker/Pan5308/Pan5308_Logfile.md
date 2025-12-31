## Pan5308
CP205 CNV calling (R120) BED file (build37) for exomedepth CNV caller step.

## add request form
R120_BEDfile_request_form.csv is added into LiveBedfiles/RequestForms
5' UTR and no padding, no additional region.

## run refgene
refgene.py was run with R120_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R120/R120_transcripts.txt --bed-format cnv --out Pan5308_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml
