## Pan5250

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R207
Pan5250_R207_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5250_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Remove duplicates
Remove the duplicated row for the same position. The duplicated rows with the genes that are not in the request form are deleted.

# Replace NA
Replace NA with the correct gene names as in the request form

# modify gene names
Modify the gene names in the additional regions to match the names in the request form