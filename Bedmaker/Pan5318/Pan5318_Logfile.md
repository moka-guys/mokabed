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

## combine beds
cat Pan5318_cnv_additional_regions.bed >> Pan5318_CNV.bed

## remove duplicated region
removed duplicated region for 	2	48034020	48034180	

## replace NA regions
replace NA with gene name from request form

## correct gene name
gene names were corrected to match the ones from request form

## testing
Generated bed was run with ED_cnv_calling_v1.6.0 and the app completed without error.

## sorting
sort -k1,1V -k2,2n Pan5318_CNV.bed -o Pan5318_CNV.beds

## testing
sorted bed was tested again. The ED app completed without error.
