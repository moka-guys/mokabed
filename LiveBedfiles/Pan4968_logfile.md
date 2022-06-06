# Pan4968 logfile
This BED file is used to contain intronic regions to be added into the TSO500 BED file
This is v2 of the intronic regions BED file (v1 is Pan4761) and contains different TERT promoter regions (these were manually added in Pan4963)

## Create file with MET regions
`cp Pan4761.bed Pan4968.bed`
delete TERT regions

## add TERT promoter regions
copy TERT promoter regions from Pan4963data.bed
manually modify TERT promoter regions to match format of MET regions already present

## manual formatting
move MET regions (chr7) to below TERT (chr5)
An empty line is at the bottom of the file so any potential concatenation of files will ensure they go onto a newline.

## Testing
the BED file was tested in UCSC