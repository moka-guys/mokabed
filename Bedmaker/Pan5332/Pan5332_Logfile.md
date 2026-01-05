## Pan5332
CP205 CNV calling (R163) BED file (build37) for exomedepth CNV caller step.

## add request form
R163_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
no UTR, no padding. No additional regions requested

## run refgene
refgene.py was run using R163_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R163/R163_transcripts.txt --bed-format cnv --out Pan5332_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## trimming 
GJB6 was manually trimmed as in Exomedepth bedfile

## testing
Generated bedfile was run with ED_cnv_calling_v1.6.0. The app completed without errors.