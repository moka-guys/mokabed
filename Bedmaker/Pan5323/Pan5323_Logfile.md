## Pan5323
CP205 CNV calling (R414) BED file (build37) for exomedepth CNV caller step.


## add request form
R414_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5'UTR, no padding. Additional regions requested

## run refgene
refgene.py was run with R414_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R414/R414_transcripts.txt --bed-format cnv --out Pan5323_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional region

## combine bed files
cat Pan5323_cnv_additional_regions.bed >> Pan5323_CNV.bed

## remove duplicate region
duplicated region was removed

## testing
generated bed file was run with ED_cnv_calling_v1.6.0. The app completed without errors.