## Pan5328
CP205 CNV calling (R79) BED file (build37) for exomedepth CNV caller step.

## add reqeust form
R79_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No padding, No UTR. Addition region was requested

## run refgene
refgene.py was run with R79_transcripts.txt, except NM_000445.3, NM_001390.4, NM_007171.3, NM_013334.3.

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R79/R79_transcripts.txt --bed-format cnv --out Pan5328_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for NM_000445.3, NM_001390.4, NM_007171.3, NM_013334.3 and additional regions

## combine bed file
cat Pan5328_cnv_additional_regions.bed >> Pan5328_CNV.bed

## remove duplicated regions
duplicated regions were removed manually

## trimming
FKRP was trimmed manually

## testing
generated bed file was tested with ED_cnv_calling_v1.6.0. The app completed without errors. 

## sorting
sort -k1,1V -k2,2n Pan5328_CNV.bed -o Pan5328_CNV.bed

## testing
generated bed was tested again. The ED app completed without error.

## reverting
It was noted that 0/1 duplicated regions should be merged instead of removal
So, git commit were reverted

## merging
0/1 duplicated regions were merged with bedtools
bedtools merge \
  -i Pan5328_CNV.bed \
  -c 4 \
  -o first \
  
## renaming
bedfiles were renamed. 
 mv Pan5328_CNV.bed Pan5328_CNV_unmerged.bed
 mv Pan5328_CNV_merged.bed Pan5328_CNV.bed

## testing
updated bed file was tested. The ED app completed without error