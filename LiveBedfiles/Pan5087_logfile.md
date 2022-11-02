This is a VCP2 R208 test BED file for CNV analysis using ExomeDepth.
Initially Pan4712_CNV.bed was created for this but needed to updated with new genes based on the Test Directory changes.

## Save query used to extract Transcript file.
Transcript was selected from the ngspanel genes table using the query select GuysAccession, Symbol, '0' as GuysAccessionVersion from ngspanelgenes where NGSPanelID=5087 This was used to create Pan5087.txt
