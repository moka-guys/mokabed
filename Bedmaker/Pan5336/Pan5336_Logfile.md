## Pan5336
CP205 CNV calling (R167) BED file (build37) for exomedepth CNV caller step

## add request form
R167_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions requested

## run refgene
refgene.py was run with R167_transcripts.txt
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R167/R167_transcripts.txt --bed-format cnv --out Pan5336_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

