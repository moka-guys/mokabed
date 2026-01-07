## Pan5327
CP205 CNV calling (R66) BED file (build37) for exomedepth CNV caller step.

## add request form
R66_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. Additional region is requested

## run refgene
refgene is run with R66_transcripts.txt except NM_001146040.1


python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R66/R66_transcripts.txt --bed-format cnv --out Pan5327_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker is run for NM_001146040.1 and additional region.

## combine bed file
 cat Pan5327_cnv_additional_regions.bed >> Pan5327_CNV.bed

## trimming
KCNA1 was trimmed manually as in exomedepth bed file