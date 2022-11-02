This is a VCP2 R207 test BED file for CNV analysis using ExomeDepth.
Initially Pan4815_CNV.bed was created for this but needed to updated to include PALB2.

## Save query used to extract Transcript file.
Transcript was selected from the ngspanel genes table using the query select GuysAccession, Symbol, '0' as GuysAccessionVersion from ngspanelgenes where NGSPanelID=5088 This was used to create Pan5088.txt