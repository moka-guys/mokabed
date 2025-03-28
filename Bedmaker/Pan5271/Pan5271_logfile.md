# Pan5271
CP2 Whole Capture BED file (build37) for coverage and variant calling.
It is a copy of Pan5239, a few issues were noted in the Pan5239_readcount.bed:
1) Bedmaker assigned NM transcripts as gene name for certain genes.
2) The additional "_" in the region labels, caused an error to be printed on ED reports. 


# Take a copy of Pan5239_exomeDepth.bed

cp Pan5239_exomeDepth.bed Pan5271_exomeDepth.bed

# Manual fix
Fix regions with genes names as transcript numbers. E.g NM_016653_1 should be MAP3K20_1

In VScode use find and replace function to replace transcript IDs to gene symbols

Only MAP3K20 and POMK had this issue.