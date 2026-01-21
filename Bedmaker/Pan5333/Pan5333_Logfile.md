## Pan5333
CP205 CNV calling (R164) BED file (build37) for exomedepth CNV caller step.

## add request form
R164_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. No additional regions is requested.

## run refgene
refgene.py was run with R164_transcripts.txt, that does not include ENST00000397985.2, NM_001042440.2, NM_001190442.1, NM_201380.2.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R164/R164_transcripts.txt --bed-format cnv --out Pan5333_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml


## run bedmaker 
ENST00000397985.2, NM_001042440.2, NM_001190442.1, NM_201380.2 were run with bedmaker

## combine bed files
cat Pan5333_cnv_additional_regions.bed >> Pan5333_CNV.bed 

## remove duplicated regions
remove regions that are duplicated in bed file

## testing 
Generated bed was run with  ED_cnv_calling_v1.6.0. The app completed without error.

## sorting
sort -k1,1V -k2,2n Pan5333_CNV.bed -o Pan5333_CNV.bed

## testing
sorted bed file was tested again. The ED app completed without error.

## remove duplicated lines
some line are different only one base just because they are 0 and 1 based. Duplicated 1 based are removed and 0 based are left.

## testing
updated bed was tested again. The ED complected without error.

## remove some transcripts regions
NM_001190442.1, NM_001042440.2, ENST00000397985.2 - these transcripts are in the request form but they are not in agreed transcripts list for CP205 readcount and CNV bedfiles. 
Regions for these transcripts are removed from the bed files. Some regions are already removed when removing duplicates previously (e.g. NM_001042440.2 does not need to be removed although it is in request as it's already removed by previous step)