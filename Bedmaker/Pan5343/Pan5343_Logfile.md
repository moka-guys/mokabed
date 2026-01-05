# Pan5343
CP205 CNV calling (R326) BED file (build37) for exomedepth CNV caller step.

# Save request form
Pan5343_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

No padding, no UTRs, and 2 additional regions specified to be included (ATM_3UTR, SMAD4_3UTR)

# Run refgene
Use Pan5343_transcript.txt to run refgene.py
```
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file ../../Bedmaker/Pan5343/Pan5343_transcript.txt --bed-format cnv --out Pan5343_CNV.bed
```

# Run bedmaker
Requested to add specified 3UTR regions to genes ATM and SMAD4. 
Saved outputs from BEDmaker.

# Add labels
Add labels to Pan5343_additional_regions_cnv.bed file

# Combine bedfiles
```
cat Pan5343_additional_regions_cnv.bed >> Pan5343_CNV.bed
```