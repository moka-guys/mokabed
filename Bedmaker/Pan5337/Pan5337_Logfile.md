## Pan5337
CP205 CNV calling (R227) BED file (build37) for exomedepth CNV caller step.

## add request form
R227_BEDfile_request_form.csv is added into LiveBedfiles/RequestForms
No UTR, no padding. No additional region is requested

## run refgene
refgene.py is run with R227_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R227/R227_transcripts.txt --bed-format cnv --out Pan5337_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
Generated bed was tested with ED_cnv_calling_v1.6.0. The app completed without error.

## sorting
sort -k1,1V -k2,2n Pan5337_CNV.bed -o Pan5337_CNV.bed