## Pan5275
CP2 Whole Capture BED file (build37) for coverage and variant calling.
It is a copy of Pan5271, a few issues were noted in the Pan5271_exomeDepth.bed:
1) The incorrect transcript was provided for the gene ABHD5, in Pan5232 the transcript was corrected to NM_016006.4 from NM_020676.5 (ABHD6 transcript).
2) We were also requested to include DMD exon 1 from NM_000109.4 transcript

# Copy Pan5271_exomeDepth.bed

cp Pan5271_exomeDepth.bed Pan5279_exomeDepth.bed

# Remove ADHD6

Manually remove ABHD6 regions using VScode

