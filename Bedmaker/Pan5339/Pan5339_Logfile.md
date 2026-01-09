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