## Pan5344
CP205 CNV calling (R332) BED file (build37) for exomedepth CNV caller step.

## add request form
R332_BEDfile_request_form.csv was added into LiveBedfiles/RequestForms
No UTR, no padding, no additional regions.

## run refgene
refgene.py was run with R332_transcripts, except for ENST00000587708.2
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R332/R332_transcripts.txt --bed-format cnv --out Pan5344_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for ENST00000587708.2

## combine bed files
cat Pan5344_cnv_additional_regions.bed >> Pan5344_CNV.bed

## remove duplicate
duplicated region was removed

## trimming
RAG1, RAG2 and GJA1 were trimmed manually as in exomedepth bed file.

## testing
generated bed was run with ED_cnv_calling_v1.6.0, and the app completed without errors

## sorting
sort -k1,1V -k2,2n Pan5344_CNV.bed -o Pan5344_CNV.bed

## testing
sorted bed was tested again. The ED app completed without errors.
