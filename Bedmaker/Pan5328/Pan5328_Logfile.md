## Pan5328
CP205 CNV calling (R79) BED file (build37) for exomedepth CNV caller step.

## add reqeust form
R79_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No padding, No UTR. Addition region was requested

## run refgene
refgene.py was run with R79_transcripts.txt, except NM_000445.3, NM_001390.4, NM_007171.3, NM_013334.3.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R79/R79_transcripts.txt --bed-format cnv --out Pan5328_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for NM_000445.3, NM_001390.4, NM_007171.3, NM_013334.3 and additional regions

## combine bed file
cat Pan5328_cnv_additional_regions.bed >> Pan5328_CNV.bed