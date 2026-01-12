## Pan5341
CP205 CNV calling (R237) BED file (build37) for exomedepth CNV caller step.

## add request form
R237_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions are requested.

## run refgene
refgene is run with R237_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R237/R237_transcripts.txt --bed-format cnv --out Pan5341_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
Generated bed was tested with ED_cnv_calling_v1.6.0 and the app completed without errors.

## sorting

sort -k1,1V -k2,2n Pan5341_CNV.bed -o Pan5341_CNV.bed
