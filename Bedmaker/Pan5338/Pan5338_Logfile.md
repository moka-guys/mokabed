## Pan5338
CP205 CNV calling (R229) BED file (build37) for exomedepth CNV caller step.

## add request form
R229_BEDfile_request_form.csv was added into /LiveBedfiles/RequestForms
No UTR, no padding. Addition regions are requested

## run refgene
refgene.py was run with R229_transcripts.txt

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R229/R229_transcripts.txt --bed-format cnv --out Pan5338_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

## run bedmaker
bedmaker was run for additional regions

## re-run bedmaker with new settings
Bedmaker was re-run as noted that 5'UTR setting should be changed at settings page.

## combine bed files
cat Pan5338new_cnv_additional_regions.bed >> Pan5338_CNV.bed

## replace NA regions
replace N/A regions with those from request form

## correct gene name and replace more NA 
correct gene names with those from request form and also replace more NA region

## trimming
trimmed FANCF gene as in exomedepth bedfile

## testing
Generated bed was tested using ED_cnv_calling_v1.6.0. The app completed without error.

## sorting
sort -k1,1V -k2,2n Pan5338_CNV.bed -o Pan5338_CNV.bed

## testing
sorted bed was tested again. The ED app completed without error.