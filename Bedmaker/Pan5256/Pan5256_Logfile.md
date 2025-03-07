## Pan5256

CP2 Exomedepth CNV calling BED file (build37) for R444.2

# Request form for R444.2
Pan5256_R444.2_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. No additional sites were added. 

# Run Bedmaker
Pan5256_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Fix N/A values
Some additionally added regions were labelled as NA. The labels were manually fixed

# Fix labelling
Some additionally added regions were labelled incorrectly. These were fixed manaully.

# Testing
Pan5256_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.