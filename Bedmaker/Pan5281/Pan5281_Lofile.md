## Pan5281
CP2 CNV calling BED file (build37) for exomedepth CNV caller step. This is to modify already generated R79 CNV bed file since a DMD region needed to be added.

# Take a copy of original R79 cnv calling bedfile
cp Pan5274_CNV.bed Pan5281_CNV.bed

# Add exon 1 of DMD (NM_000109.4)

We currently use NM_004006.2 for DMD, however we have been requested to add exon 1(NM_000109.4)

Rebecca Haines used UCSC and IGV to obtain the exon 1 coordinates (chrX:33357376-33357505), these were manually added to Pan5281_CNV.bed

The exon was not padded to be consistent with the rest of the regions in the bedfiles.

# Sort bedfiles

Pan5281_CNV.bed were sorted to ensure the region is placed in order.

sort Pan5281_CNV.bed -k1,1V -k2,2n -k3,3n > Pan5281_sorted.bed;mv Pan5281_CNV.bed Pan5281_unsorted.bed; mv Pan5281_sorted.bed Pan5281_CNV.bed; rm Pan5281_unsorted.bed