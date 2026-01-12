## Pan5313
CP205 CNV calling (R134) BED file (build37) for exomedepth CNV caller step.

# Save request form
R134_BEDfile_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. No additional region included

# run refgene.py

Use R134_transcript.txt to run refgene.py
python3 /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/refgene.py --refgene /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/ncbiRefSeq.txt --transcript-file /home/win/Desktop/workspace/generate_bed/CP205/R134/R134_transcripts.txt --bed-format cnv --out Pan5313_CNV.bed --config /home/win/Desktop/clone_github/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/config.yaml

### no need to run bedmaker since there in no additional regions.

# test bed file
Generated bed file was tested on DNAnexus by running ED_cnv_calling_v1.6.0 and The app completed successfully without any error.


## sorting
sort -k1,1V -k2,2n Pan5313_CNV.bed -o Pan5313_CNV.bed

## testing
sorted bed was tested again and the ED app completed without error.