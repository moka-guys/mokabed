## Pan5245

CP2 Exomedepth CNV calling BED file (build37) for R229

# Request form for R229
Pan5245_R229_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Multiple additional regions in request form

# Run Bedmaker
Pan5245_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Fix N/A values
Some additionally added regions were labelled as NA. The labels were manually fixed

# Fix labelling
Some additionally added regions were labelled incorrectly. These were fixed manaully.

# Testing
Pan5245_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.

