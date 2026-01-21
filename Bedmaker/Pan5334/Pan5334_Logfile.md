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

## remove duplicated regions
duplicated regions are removed from bed file

## trimming
GJB2, GJB6 and GJA1 were trimmed as in exomedepth bed file manually

## testing
Generated bed was tested with ED_cnv_calling_v1.6.0 and the app completed without errors

## sorting
sort -k1,1V -k2,2n Pan5334_CNV.bed -o Pan5334_CNV.bed

## testing
sorted bed was tested again. The ED app completed without error.

## reverting
It was found that 0/1 based duplicated regions should be merged rathar than removing them.
Commit were reverted until the stage where 0/1 based removal was done.
Invalid transcripts removal commit was also reverted althogh it was the correct commit since this commit is after 0/1 based duplicates removal. Therefore, invalid transcript removal step needs to redo

## remove some transcripts regions
NM_001190442.1, NM_001042440.2, ENST00000397985.2 - these transcripts are in the request form but they are not in agreed transcripts list for CP205 readcount and CNV bedfiles. 
Regions for these transcripts are removed from the bed files.
grep -v -E "NM_001190442.1|NM_001042440.2|ENST00000397985.2" Pan5334_CNV.bed > Pan5334_CNV_clean.bed

## merging
0/1 duplicated regions were merged using bedtools
bedtools merge \
  -i Pan5334_CNV_clean.bed \
  -c 4 \
  -o first \
  > Pan5334_CNV_merged.bed

## renaming
 mv Pan5334_CNV.bed Pan5334_CNV_unclean_unmerged.bed
 mv Pan5334_CNV_merged.bed Pan5334_CNV.bed