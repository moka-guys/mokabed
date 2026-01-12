## Pan5316
CP205 CNV calling (R207) BED file (build37) for exomedepth CNV caller step.

## add request form
R207_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms.
5 UTR needed. No padding. Additional regions requested. 

## run refgene
refgene.py was run with R207_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R207/R207_transcripts.txt --bed-format cnv --out Pan5316_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions.

## combine bed files
cat Pan5316_cnv_additional_regions.bed >> Pan5316_CNV.bed
## remove duplicates
duplicated region was removed

## replace NA
NA regions were replaced with gene names from request form

## correct gene name
gene names were correct to match with request form

## testing
generated bed was tested with ED_cnv_calling_v1.6.0. The app completed without errors.

## sorting
sort -k1,1V -k2,2n Pan5316_CNV.bed -o Pan5316_CNV.bed