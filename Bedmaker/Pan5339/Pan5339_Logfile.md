## Pan5339
CP205 CNV calling (R230) BED file (build37) for exomedepth CNV caller step.

## add request form
R230_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. Additional regions requested.

## update request form manually
The file name of request form is R230_BEDfile_request_form.csv and this is for Pan5339. But inside the file, it was mentioned as R236 and Pan5340. Discussed with Rebecca and checked MOKA. Confirmed that R230 and Pan5339 are correct. So manually update them on request form. Heidi was informed about this. 

## run refgene
refgene.py was run with R230_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R230/R230_transcripts.txt --bed-format cnv --out Pan5339_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions

## combine bed files
cat Pan5339_cnv_additional_regions.bed >> Pan5339_CNV.bed

## replace NA
NA regions were replaced with gene names from request form

## correct gene name
gene names were corrected as in request form

## testing
generated bed file was tested with ED_cnv_calling_v1.6.0. The app completed without error.

## sorting
sort -k1,1V -k2,2n Pan5339_CNV.bed -o Pan5339_CNV.bed