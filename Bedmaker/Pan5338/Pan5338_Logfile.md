## Pan5338
CP205 CNV calling (R229) BED file (build37) for exomedepth CNV caller step.

## add request form
R229_BEDfile_request_form.csv was added into /LiveBedfiles/RequestForms
No UTR, no padding. Addition regions are requested

## run refgene
refgene.py was run with R229_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R229/R229_transcripts.txt --bed-format cnv --out Pan5338_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions

## re-run bedmaker with new settings
Bedmaker was re-run as noted that 5'UTR setting should be changed at settings page.
