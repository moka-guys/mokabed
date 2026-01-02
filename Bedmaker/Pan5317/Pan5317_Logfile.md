## Pan5317
CP205 CNV calling (R208) BED file (build37) for exomedepth CNV caller step.

## added request form
R208_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms

5' UTR is added, no padding. Additional regions were requested

# run refgene
refgene.py was run using R208_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R208/R208_transcripts.txt --bed-format cnv --out Pan5317_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

# run bedmaker 
bedmaker was run for additional regions requested. 

# combine two bed files
cat Pan5317_cnv_additinal_regions.bed >> Pan5317_CNV.bed

# remove duplication
remove duplicated region for 11	108239720	108239839	

# replace NA with correct gene name from the request form
replace NA for 13	32974296	32974415

# rename gene
rename gene to match with those from request form

# testing
Generated bed file was run with ED_cnv_calling_v1.6.0. The app finished without error.