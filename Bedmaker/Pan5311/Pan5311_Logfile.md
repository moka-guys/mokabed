## Pan5311
CP205 CNV calling (R123) BED file (build37) for exomedepth CNV caller step.

## add request form
R123_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms.
5 UTR only. No padding. No additional regions requested.

## run refgene
refgene.py was run with R123_transcripts.txt.
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R123/R123_transcripts.txt --bed-format cnv --out Pan5311_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
generated bed was run with ED_cnv_calling_v1.6.0. The app completed without errors.

## sorting
sort -k1,1V -k2,2n Pan5311_CNV.bed -o Pan5311_CNV.bed

## testing
sorted bed file was tested again. The ED app completed without errors.