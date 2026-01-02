## Pan5320
CP205 CNV calling (R211) BED file (build37) for exomedepth CNV caller step.

## add request form
R211_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5' UTR only, no padding. Additional regions were requested

## run refgene
refgene.py was run with R211_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R211/R211_transcripts.txt --bed-format cnv --out Pan5320_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions.

## combine bedfiles
cat Pan5320_cnv_additional_regions.bed >> Pan5320_CNV.bed

## remove duplicated regions
remove duplicated regions that are not in request form

## replace N/A
replace N/A with correct gene names from request form