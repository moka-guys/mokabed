# Pan5269
This BED file is for R444.1 CNV calling. It is a copy of Pan5183 with the additional regions removed. The BED file should only contain BRCA1, BRCA2 and PALB2

## Create the BED file
`cp Pan5183_CNV.bed Pan5269_CNV.bed`

## Remove genes no longer required
- ATM
- RAD51D
- RAD51C
- CHEK2

## test BED file
Testing performed in 003_250325_Pan5269_testing
Reports produced as expected with only BRCA1, BRCA2 and PALB2 regions shown

# Move Pan5269 to correct folder

mv Pan5269_CNV.bed ../Bedmaker/Pan5269
mv Pan5269_logfile.md ../Bedmaker/Pan5269