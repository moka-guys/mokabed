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