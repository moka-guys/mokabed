This BED file contains a list of intronic CNV regions specific to R210 on VCP3 panel.
The coordinates were taken from Pan3610

## The following regions were requested by MYau
MSH2_3UTR;MSH6_3UTR;MLH1_3UTR;EPCAM_3UTR;PMS2_3UTR

## Copy of Pan3610.bed
cp Pan3610.bed Pan4765.bed

## Manually edit Pan4765.bed
Remove additional intronic regions, only keep regions specified by MYau

# Sort bedfile
sort LiveBedfiles/Pan4765.bed -k1,1V -k2,2n -k3,3n > LiveBedfiles/Pan4765.sorted.bed && mv LiveBedfiles/Pan4765.sorted.bed LiveBedfiles/Pan4765.bed
