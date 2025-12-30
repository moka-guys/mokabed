## Pan5317
CP205 CNV calling (R208) BED file (build37) for exomedepth CNV caller step.

## added request form
R208_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms

5' UTR is added, no padding. Additional regions were requested

# run refgene
refgene.py was run using R208_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R208/R208_transcripts.txt --bed-format cnv --out Pan5317_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

# run bedmaker 
bedmaker was run for additional regions requested. 