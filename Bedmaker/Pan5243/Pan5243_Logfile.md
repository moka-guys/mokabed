## Pan5243

CP2 Exomedepth CNV calling BED file (build37) for R414

# Request form for R414
Pan5243_R414_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. No additional sites were added. 

# Run Bedmaker
Pan5243_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Manually edit CNV bedfile 
Duplicate overlapping region (5	112181828	112181947	CTC-554D6.1;ENSG00000258864) was added by bedmaker, these were manually removed.

# Testing
Pan5243_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.