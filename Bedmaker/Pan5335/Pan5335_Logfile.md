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

## trimming
GJB2 and GJA1 were trimmed manually as in exomedepth bedfile

## testing
Generated bed file was tested with ED app. The app completed without errors.

## sorting
sort -k1,1V -k2,2n Pan5335_CNV.bed -o Pan5335_CNV.bed

## testing
sorted bed file was tested again. The ED app completed without error

## reverting
It was found out that 0/1 duplicated regions should be merged rather than removing those lines.
Commits were reverted until 0/1 duplicated region removal commit.
Invalid transcript removal commit was also reverted as that step was done after 0/1 duplicates removal. But it was a correct step so needs to redo

## removing invalid transcripts
NM_001190442.1, NM_001042440.2, ENST00000397985.2 - these transcripts are in the request form but they are not in agreed transcripts list for CP205 readcount and CNV bedfiles. 
Regions for these transcripts are removed from the bed files.
grep -v -E "NM_001190442.1|NM_001042440.2|ENST00000397985.2" Pan5335_CNV.bed > Pan5335_CNV_clean.bed