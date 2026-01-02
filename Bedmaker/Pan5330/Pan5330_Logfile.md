## Pan5330
CP205 CNV calling (R90) BED file (build37) for exomedepth CNV caller step.

## add request form
R90_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions are requested.

## run refgene
refgene.py was run with R90_transcripts.txt
NM_001083899.1 from request from in not Mane transcript. So, it is not included in ncbiRefSeq.txt. So that transcript was not included when running refgene.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R90/R90_transcripts.txt --bed-format cnv --out Pan5330_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
The excluded transcript NM_001083899.1 above is NM_016363.5 in hg19. It was run on Bedmaker

# combine bed files
cat Pan5330_cnv_additional_regions.bed >> Pan5330_CNV.bed

# remove duplicated regions
duplicated region is removed 

## trimming
CHST14, BLOC1S3, THBD, P2RY12 genes were trimmed

## testing
Generated bed file was tested with ED_cnv_calling_v1.6.0. The app completed without error.