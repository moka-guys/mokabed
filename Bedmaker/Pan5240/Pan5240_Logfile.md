## Pan5240

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R66
Pan5240_R66_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. No additional sites was added. 

# Run Bedmaker
Pan5240_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Testing
Pan5240_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.

# Re-run Bedmaker 
BedMaker was re-run since the bed file should be made with transcript, not with the Gene name. 
The old Pan5240_CNV.bed made with Gene name was deleted, and replaced with new Pan5240_cnv.bed. The query.json file is also updated.

# Re-test
After re-generating the bed file with transcripts, the new bed file was re-tested with ED_cnv_calling_v1.4.0. The app completed successfully without any error.
