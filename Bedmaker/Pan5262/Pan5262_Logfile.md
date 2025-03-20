## Pan5262

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R326
Pan5262_R236_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used. Additional sites were added.

# Run Bedmaker
Pan5262_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Manually edit CNV bedfile 
Duplicate overlapping region (C11orf65;ENSG00000166323 and FBXO11;ENSG00000138081) was added by bedmaker, this was manually removed.

# Fix labels

Manually fix additional regions labels
