## Pan5249

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R208
Pan5249_R208_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5249_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Remove duplicates
Remove the duplicated row for the same position. The duplicated rows with the genes that are not in the request form are deleted.

# Replace NA
Replace NA with the correct gene names as in the request form

# modify gene names
Modify the gene names in the additional regions to match the names in the request form
# Testing
Pan5249_cnv.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.

# Remove ATM_3UTR
ATM_3UTR has poor coverage, which resulted in errors in the Exomedepth CNV report. 
M.Yau confirmed the regions is okay to remove.

ATM_3UTR	chr11:108239720-108239839

The region above was manually removed from Pan5249_CNV.bed

# Testing
Pan5249_cnv.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error on the report.