# Pan4968 logfile
This BED file is used to contain intronic regions to be added into the TSO500 BED file
This is v2 of the intronic regions BED file (v1 is Pan4761) and contains different TERT promoter regions (these were manually added in Pan4963)
The MET regions are specified in the BED file request form for Pan4761
The TERT regions are specified in the BED file for PAN4963

## Create bed file
Copy Pan4761.bed as base file `cp Pan4761.bed Pan4968.bed`

## MET regions
Required MET regions are unchanged from Pan4761 but TERT regions are different.
Manually delete TERT region from Pan4968.bed

## TERT regions
Manually copy required TERT regions from Pan4963data.bed

## Formatting
manually modify TERT promoter regions to match format of MET regions already present
move MET regions (chr7) to below TERT (chr5)
An empty line is at the bottom of the file so any potential concatenation of files will ensure they go onto a newline.
