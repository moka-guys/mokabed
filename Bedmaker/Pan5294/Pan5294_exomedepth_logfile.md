## Pan5294_exomedepth
CP205 Whole Capture BED file (build37) for CNV calling using Exomedepth

The bedfile consists of 

- VCP1/VCP2 genes- no padding but include 5UTR
- VCP3/CP205 genes + non R code genes- no padding
- FXR1 non-coding region provided in FXR1_noncoding_region.txt. This region is for the muscle specific transcript described in https://doi.org/10.1038/s41467-019-08548-9
- DMD_ex1.txt: DMD exon1 from NM_000109.4
- Pan5294_CNVintronictargets.csv: known CNV intronic targets.

Lists produced by R Haines and N Pinto using information from Heidi and Michael. 

# Save updated refgene.py
refgene.py was updated to create exomedepth readcount bedfiles.

# Make VCP1/VCP2 bedfile + non R code genes
Run refgene.py to create bedfile with no padding and 5UTR. 

python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file /home/natashapinto/Desktop/mokabed/Bedmaker/Pan5294/Pan5294_VCP1_VCP2_transcripts.txt --bed-format exomedepth --out Pan5294_VCP1_VCP2_exomeDepth.bed

# Remove "_" from 5UTR names
Exomedepth uses "_" to split the genes name and exon number, any additional "_" returns an error on the reports. Use VScode find and replace "_5UTR" to "-5UTR" 

# Make VCP3/CP205 bedfile
Run refgene for VCP3 and CP205 genes with no padding and no UTRs

python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file /home/natashapinto/Desktop/mokabed/Bedmaker/Pan5294/Pan5294_VCP3_CP205_transcripts.txt --bed-format exomedepth --out Pan5294_VCP3_CP205_exomeDepth.bed

# Run bedmaker for non_MANE and nonRgenes
From our previous attempts to create the variant calling and coverage bedfiles using refgene we know refseq gene was unable to find the following transcripts, because they are not MANE: Transcript(s) not found in ncbiRefSeq.txt: NM_000445.3, NM_001083899.1, NM_001130103.1, NM_001146040.1, NM_001390.4, NM_002584.2, NM_007171.3, NM_013334.3, NM_022068.2, NM_138569.2, NM_201380.2

A seperate bedfile will be created using these transcripts (VCP3_CP205_nonMANETranscripts.txt) and Pan5294_nonRcode_genes.txt

Run bedmaker and save the outputs

# Run bedmaker for additional regions
FXR1_noncoding_region.txt DMD_ex1.txt Pan5294_CNVintronictargets.csv
Run bedmaker and save the outputs

# Fix overlapping regions
When generating the bedfile bedmaker highlighted the following regions that overlapped multiple genes: 

chr2:48034020-48034180 overlap was between MSH6(gene of interest) and FBXO11. The overlap was due to the genes being on opposite-strands. The duplicated region on FBX011 was manualy deleted in VScode and gene label was changed MSH6_3UTR

chr5:112181828-112181947 overlap was between APC(gene of interest) and CTC. The overlap was due to the genes being on opposite-strands. The duplicated region on CTC was manualy deleted in VScode and gene label was changed APC_3UTR.

chr11:108239720-108239839 overlap was between ATM(gene of interest) and C11orf65. The overlap was due to the genes being on opposite-strands. The duplicated region on C11orf65 was manualy deleted in VScode and gene label was changed ATM_3UTR.

chr15:33010462-33010561 overlap was between GREM1(gene of interest) and RP11. The overlap was due to the genes being on opposite-strands. The duplicated region on RP11 was manualy deleted in VScode and gene label was changed GREM1-SCG5_13.

chr15:33010635-33010953 overlap was between GREM1(gene of interest) and RP11. The overlap was due to the genes being on opposite-strands. The duplicated region on RP11 was manualy deleted in VScode and gene label was changed GREM1-SCG5_14.

chr17:56431028-56431147 overlap was between RNF43(gene of interest) and BZRAP1-AS1. The overlap was due to the genes being on opposite-strands. The duplicated region on BZRAP1-AS1 was manualy deleted in VScode and gene label was changed RNF43_3UTR.

chr19:1228320-1228439 overlap was between STK11(gene of interest) and C19orf26. The overlap was due to the genes being on opposite-strands. The duplicated region on C19orf26 was manualy deleted in VScode and gene label was changed STK11_3UTR.

# Fix NA regions
CNV intronic targets were labelled as N/A, the correct label was taken from Pan5294_CNVintronictargets.csv

# Remove unrequired regions
Bedmaker added genes from overlapping regions, which aren't regions of interest. 19 50921285 50921404 CTD-2545M3.6_ 15 33010004 33010104 RP11-758N13.1_

# Fix labelling
A few CNV intronic targets had incomplete labels, these were fixed manually.

# Add POLD1 region back
To ensure all regions in Pan5294_CNVintronictargets.csv were included, a manual search was performed for each region. During this search it was noticed the POLD1_3UTR chr19:50921285-50921404 and GREM1_SCG5_12 chr15:33010004-33010104 were missing. The region was accidentally removed during as they were thought to be overlapping regions (see section "remove unrequired regions").

# Remove chr prefix
bedfiles made by refgene.py had a 'chr' prefix and bedmaker bedfiles didn't. 'Chr' prefix removed using VScode

# Check for duplicated regions
A few genes have multiple transcripts requested, this has resulted in duplicated regions in the bedfiles.

Bedtools merge will be used to remove overlapping regions.

First combine Pan5294_VCP3_CP205_exomeDepth.bed and Pan5294_nonMANEnonR_exomeDepth.bed
NOTE: Pan5294_VCP1_VCP2_exomeDepth.bed wasn't combined as we didn't want to merge the 5UTR regions.

cat Pan5294_nonMANEnonR_exomeDepth.bed >> Pan5294_VCP3_CP205_exomeDepth.bed

sort the bedfile
sort -k1,1V -k2,2n -k3,3n Pan5294_VCP3_CP205_exomeDepth.bed > Pan5294_VCP3_CP205_exomeDepth_sorted.bed

bedtools merge
-c- keep column 4
-o first- choose the first value
bedtools merge -i Pan5294_VCP3_CP205_exomeDepth_sorted.bed -c 4 -o first > Pan5294_VCP3_CP205_exomeDepth_sorted_merged.bed

# Combine VCP1/VCP2 bedfile and additional regions bedfiles
cat Pan5294_VCP1_VCP2_exomeDepth.bed Pan5294_additionalregions_exomeDepth.bed >> Pan5294_VCP3_CP205_exomeDepth_sorted_merged.bed

rename Pan5294_VCP3_CP205_data_sorted_merged.bed
mv Pan5294_VCP3_CP205_exomeDepth_sorted_merged.bed Pan5294_exomeDepth.bed

# sort bedfile
sort Pan5294_exomeDepth.bed -k1,1V -k2,2n -k3,3n > Pan5294_exomeDepth_sorted.bed; mv Pan5294_exomeDepth.bed Pan5294_exomeDepth_unsorted.bed; mv Pan5294_exomeDepth_sorted.bed Pan5294_exomeDepth.bed; rm Pan5294_exomeDepth_unsorted.bed

# Check labelling of additional regions

3UTR regions were missing exon numbering, these were added manually in VScode.