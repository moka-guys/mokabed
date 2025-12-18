## Pan5301
CP205 CNV calling (R73) BED file (build37) for exomedepth CNV caller step.

# Save request form
Pan5301_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. DMD_ex1 additional region included

# Save updated refgene.py 
Script has been updated to support generation of CNV calling bedfiles

# Run refgene.py
Use Pan5301_transcript.txt to run refgene.py
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file Pan5301_transcript.txt --bed-format cnv --out Pan5301_CNV.bed

# Run bedmaker for additional region
Requested to add DMD_ex1 to R73 CNV calling bed

Save outputs from Bedmaker
