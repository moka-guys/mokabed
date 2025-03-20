## Pan5259

CP2 CNV calling BED file (build37) for exomedepth CNV caller step.

# Request form for R326
Pan5259_R326_bedrequest.txt was used  (added into mokabed/LiveBedfiles/RequestForms)

5UTR was included for all genes and no padding was used and additional sites was added.

# Run Bedmaker
Pan5259_CNV_query.json contains the original query given to bedmaker to generate the bedfile.

# Manually edit CNV bedfile 
Duplicate overlapping region 11	108239720	108239839	C11orf65;ENSG00000166323 was added by bedmaker, this was manually removed.