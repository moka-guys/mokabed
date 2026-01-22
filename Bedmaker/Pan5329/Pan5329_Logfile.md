## Pan5329
CP205 CNV calling (R81) BED file (build37) for exomedepth CNV caller step.

## add request form
R81_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding. Additional regions was requested. 

## run refgene
refgene was run with R81_transcripts.txt, except NM_001130103.1, NM_002584.2, NM_022068.2, NM_138569.2

 python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R81/R81_transcripts.txt --bed-format cnv --out Pan5329_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

 ## run bedmaker 
 bedmaker was run for NM_001130103.1, NM_002584.2, NM_022068.2, NM_138569.2 and additional regions

 ## combine bed files
 cat Pan5329_cnv_additional_regions.bed >> Pan5329_CNV.bed

 ## remove duplicates
 duplicated regions were removed from bed file

 ## trimming
 manual trimming was done for KBTBD13 as in Exomedepth bed file. 

 ## testing
 Generated bed file was run with ED_cnv_calling_v1.6.0. The app completed without error.

 ## sorting
 sort -k1,1V -k2,2n Pan5329_CNV.bed -o Pan5329_CNV.bed

 ## testing
 sorted bed was tested again. The ED app completed without error. 

 ## revert the 0/1based duplications
 It was found out that 0/1 duplication should be merged instead of removing.
 The commit was reverted back before the step of remove 0/1 based duplications

 ## merging
 Bedtools merge will be used to remove overlapping regions.
 bedtools merge -i Pan5329_CNV.bed -c 4 -o first > Pan5329_CNV_merged.bed

 ## renaming files
 Pan5329_CNV.bed, the file before merging, was renamed as Pan5329_CNV_unmerged.bed
 Pan5329_CNV_merged.bed was renamed as Pan5329_CNV.bed
 mv Pan5329_CNV.bed Pan5329_CNV_unmerged.bed
 mv Pan5329_CNV_merged.bed Pan5329_CNV.bed

 ## testing
 updated bed was tested with ED app. The app completed without errors.