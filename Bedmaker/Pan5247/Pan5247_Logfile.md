## Pan5247

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R211
Pan5247_R211_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5247_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Remove duplicated rows
Duplicated pos are removed based on the request form. The gene that are not in the request form (in duplicated rows) are deleted

# Replace NA
NA are replaced with correct gene names as in request form. The relevant ENSG number are obtained from Ensembl.

# Replace correct gene name as in request from
The subfix are some gene names are manually modified for additional regions to match with request form (for example, MSH2 is replace with MSH2_EPCAM_1 in chr2:47616487-47616586)
