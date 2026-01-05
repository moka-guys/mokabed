## Pan5335
CP205 CNV calling (R166) BED file (build37) for exomedepth CNV caller step.

## add request form
R166_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions requested

## run refgene
refgene.py was run with R166_transcripts.txt, except  ENST00000397985.2, NM_001042440.2, NM_001190442.1.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R166/R166_transcripts.txt --bed-format cnv --out Pan5335_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
run bedmaker for ENST00000397985.2, NM_001042440.2, NM_001190442.1.

## combine bed files
cat Pan5335_cnv_additional_regions.bed >> Pan5335_CNV.bed

## remove duplicates
duplicated regions are removed