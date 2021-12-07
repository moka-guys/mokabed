Pan4711 is a panel wide BED file for VCP2 used for exomedepth.

Initially Pan4301exomedepth.bed was created for this but it was noticed the BED file did not contain the required intronic CNV regions.


## Get a copy of Pan4301data.bed at the commit where additional BED files were being added

Manually get a copy from this commit fcc9bedf2d and name it as Pan4771data.bed
https://github.com/moka-guys/mokabed/blob/fcc9bedf2d825c5b159c585f0543f74b19ac6c94/LiveBedfiles/Pan4301data.bed


## Add missed intronic sites for CNV BED file- Pan3610
cat Pan3610.bed >> Pan4771data.bed

## generate intermediary BED4 file for capture regions
cut -f1-4 ../Pan4771data.bed > _Pan4771.bed

## generate intermediary exomedepth files for exons
./makeExomedepth.sh hg19 __Pan4771  _Pan4771.bed

## set sorted list of missed (non-exonic) capture regions
sort -k1,1 -k2n,3n __Pan4771_missed.bed > __Pan4771_extra.bed

## amend missed (non-exonic) regions with:
# 1. exomedepth compatible names (no underscores)
# 2. strand information (BED6)
vi __Pan4771_extra.bed

# regenerate (final) exomedepth files giving the additional non-exonic regions from last step
./makeExomedepth.sh hg19 Pan4771 _Pan4771.bed __Pan4771_extra.bed

# NB the final step should not yield any missed regions
