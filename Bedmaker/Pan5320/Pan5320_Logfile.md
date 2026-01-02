## Pan5320
CP205 CNV calling (R211) BED file (build37) for exomedepth CNV caller step.

## add request form
R211_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
5' UTR only, no padding. Additional regions were requested

## run refgene
refgene.py was run with R211_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R211/R211_transcripts.txt --bed-format cnv --out Pan5320_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions.

## combine bedfiles
cat Pan5320_cnv_additional_regions.bed >> Pan5320_CNV.bed

## remove duplicated regions
remove duplicated regions that are not in request form

## replace N/A
replace N/A with correct gene names from request form

## correct gene name
correct gene name to match those from request form

## run ref gene for addition MUTYH gene
Noted that 2nd transcript for MUTYH gene NM_001128425.2 was missed while running refgene previously.
Refgene was run again with mutyh_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R211/mutyh_transcripts.txt --bed-format cnv --out Pan5320_mutyh_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## combine bed files
cat Pan5320_mutyh_CNV.bed >> Pan5320_CNV.bed

## remove duplicated regions
remove duplicated regions after combining bed files

## trimming

trimmed GREM1 gene as in exomedepth bed file

## testing

Generated bed file was tested with ED_cnv_calling_v1.6.0 and the app completed without errors

## modify gene name to be consistent with others
GREM1-5UTR_2 is updated to GREM1_5UTR2








