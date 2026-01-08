## Pan5326
CP205 CNV calling (R444.2) BED file (build37) for exomedepth CNV caller step.

## add request form
R444.2_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5 UTR, no padding. Additional regions requested.

## run refgene
refgene.py was run with R4442_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R4442/R4442_transcripts.txt --bed-format cnv --out Pan5326_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions.

## combine bed files
cat Pan5326_cnv_additional_regions.bed >> Pan5326_CNV.bed