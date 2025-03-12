## Pan5253

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R81
Pan5253_R81_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional site was added.

# Run Bedmaker
Pan5253_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# modify gene names
Modify the gene name in the additional regions to match the name in the request form

# Testing
Pan5253_cnv.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.
