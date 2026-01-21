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

## reverting
It was noted that 0/1 duplicated regions should be merged instead of removal
So, git commit were reverted until 0/1 duplicated removal step. In doing so, removal of invalid transcripts was also reverted since this step was done after 0/1 duplicated removal. So, invalid transcript removal step will be re-added in the updated PR

## remove some transcripts regions
NM_001190442.1, NM_001042440.2, ENST00000397985.2 - these transcripts are in the request form but they are not in agreed transcripts list for CP205 readcount and CNV bedfiles. 
Regions for these transcripts are removed from the bed files.
grep -v -E "NM_001190442.1|NM_001042440.2|ENST00000397985.2" Pan5333_CNV.bed > Pan5333_CNV_clean.bed

## merging duplicated regions
bedtools was used to merged 0/1 based duplicated regions
bedtools merge \
  -i Pan5333_CNV_clean.bed \
  -c 4 \
  -o first \
  > Pan5333_CNV_merged.bed