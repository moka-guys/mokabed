## Pan5315
CP205 CNV calling (R337) BED file (build37) for exomedepth CNV caller step.

## add request form
R337_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms.
5' UTR only, no padding. No additional region requested.

## run refgene
refgene.py was run with R337_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R337/R337_transcripts.txt --bed-format cnv --out Pan5315_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## testing
Generated bed file was run with ED_cnv_calling_v1.6.0 and the app completed without errors.
