## Pan5351
CP205 CNV calling bed file for R236, to be used for Exomedepth 

## Copy Pan5340 to Pan5351
Pan5340_CNV.bed is existing bed file for R236. To make additional changes, Pan5340 was copied into Pan5351

cp ../Pan5340/Pan5340_CNV.bed ./Pan5351_CNV.bed

## run refgene.py
refgene.py was run using NM_000057.4 for BLM gene

python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/clone_github/mokabed/Bedmaker/Pan5351/BLM_transcript.txt --bed-format cnv --out Pan5351_BLM_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml
## combine bed files
cat Pan5351_BLM_CNV.bed >> Pan5351_CNV.bed
## sorting
sort -k1,1V -k2,2n Pan5351_CNV.bed -o Pan5351_CNV.bed
## testing
Bed file was tested with ED_cnv_calling_v1.7.0 and the app finished without error. 

## add request form
R236_BEDfile_request_form_april2026.csv was added into mokabed/LiveBedFiles.
In the request form the newly added transcript for BLM is NM_000057.4.
