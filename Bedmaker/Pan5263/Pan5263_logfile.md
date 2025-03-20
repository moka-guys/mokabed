## Pan5263

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R230
Pan5263_R230_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5263_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Fix labels

Manually fix additional regions labels

# Testing
Pan5263_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.