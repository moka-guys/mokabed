## Pan5334
CP205 CNV calling (R165) BED file (build37) for exomedepth CNV caller step.

## add request form
R165_BEDfile_request_form.csv was added into /LiveBedfiles/RequestForms

No UTR, no padding. No additional regions were requested

## run refgene
refgene.py was run with R165_transcripts.txt, except ENST00000397985.2, NM_001042440.2, NM_001190442.1.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R165/R165_transcripts.txt --bed-format cnv --out Pan5334_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
run bedmaker for ENST00000397985.2, NM_001042440.2, NM_001190442.1. 

## combine bed files
cat Pan5334_cnv.bed >> Pan5334_CNV.bed