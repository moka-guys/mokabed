## Pan5254

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R79
Pan5254_R79_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. No additional sites was added.

# Run Bedmaker
Pan5254_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Testing
Pan5254_cnv.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.

# Correct the gene name for POMK to match with request form
The NM_032237 was replaced with POMK to match with request form 
# Re-testing
Pan5254_cnv.bed was re-tested after update for POMK in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.