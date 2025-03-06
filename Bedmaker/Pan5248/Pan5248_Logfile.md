## Pan5248

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R210
Pan5248_R210_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5248_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Remove duplicates
Remove the duplicated row for the same position. The duplicated rows with the genes that are not in the request form are deleted.

# Replace NA
Replace NA with the correct gene names as in the request form. The ENSG number is obtained from Ensembl.

# modify gene names
Modify the gene names in the additional regions to match the names in the request form

# Testing
Pan5248_cnv.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.

