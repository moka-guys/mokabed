## Pan5279
CP2 Whole Capture BED file (build37) for coverage and variant calling.
It is a copy of Pan5271, a few issues were noted in the Pan5271_exomeDepth.bed:
1) The incorrect transcript was provided for the gene ABHD5, in Pan5232 the transcript was corrected to NM_016006.4 from NM_020676.5 (ABHD6 transcript).
2) We were also requested to include DMD exon 1 from NM_000109.4 transcript

# Copy Pan5271_exomeDepth.bed

cp Pan5271_exomeDepth.bed Pan5279_exomeDepth.bed

# Remove ADHD6

Manually remove ABHD6 regions using VScode

# Run Bedmaker
Pan5279_ABHD5_bedfile_query.json contains the original query given to bedmaker to generate ABHD5 the bedfiles.

# Combine ABHD5 regions with Pan5271_exomeDepth.bed

cat Pan5279ABHD5_exomeDepth.bed >> Pan5279_exomeDepth.bed

# Add exon 1 of DMD (NM_000109.4)

We currently use NM_004006.2 for DMD, however we have been requested to add exon 1(NM_000109.4)

Rebecca Haines used UCSC and IGV to obtain the exon 1 coordinates (chrX:33357376-33357505), these were manually added to Pan5279_exomeDepth.bed

The exon was not padded to be consistent with the rest of the regions in the bedfiles.

# Sort bedfiles

Pan5279_exomeDepth.bed were sorted to ensure the region is placed 

sort Pan5279_exomeDepth.bed -k1,1V -k2,2n -k3,3n > Pan5279_sorted.bed;mv Pan5279_exomeDepth.bed Pan5279_unsorted.bed; mv Pan5279_sorted.bed Pan5279_exomeDepth.bed; rm Pan5279_unsorted.bed

# Testing 
Pan5279_exomeDepth.bed was tested in DNAnexus using ED_readcount_analysis_v1.3.0 and ED_cnv_calling_v1.3.0. The apps completed successfully without any errors.

# Fixes

A few issues were spotted during code review
1) Add tab between chromosome and start coordinate (3	43732375	43732531)
2) Changed name of a region from DMD-ex1_1 to DMD-Dp427C_1
3) Remove 3 that was added accidentatly to F8_1 (F8_13 to F8_1)
4) Fix typo in logfile (Header changed from Pan5275 to Pan5279)
 