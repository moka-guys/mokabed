## Pan5239

CP2 Whole Capture BED file (build37) for exomedepth readcount step.

# Files included
Pan5239_CP2transcripts.csv- Genes that are included in R code tests that will be tested on CP2, provided as a transcript ID with a version
Pan5239_nonRgenes.csv- Genes that are not included on R code tests at the moment, provided as gene name. BEDmaker will select the MANE transcript equivalent or the Ensembl canonical transcript if the MANE equivalent is unavailable.
Pan5239_FXR1regions.csv- FXR1 non-coding region
Pan5239_CNVintronictargets.csv- known CNV intronic targets.

5UTR was included for all genes and no padding was added

# Run Bedmaker
Pan5239_exomedepth_query.json contains the original query given to bedmaker to generate the bedfile.

# Fix overlapping regions
When generating the bedfile bedmaker highlighted the following regions that overlapped multiple genes:
chr2:48034020-48034180
chr5:112181828-112181947
chr11:108239720-108239839
chr15:33010462-33010561
chr15:33010635-33010953
chr17:56431028-56431147
chr19:1228320-1228439

chr2:48034020-48034180 overlap was between MSH6(gene of interest) and FBXO11. The overlap was due to the genes being on opposite-strands. The duplicated region on FBX011 was manualy deleted in VScode and gene label was changed MSH6_3UTR

chr5:112181828-112181947 overlap was between APC(gene of interest) and CTC. The overlap was due to the genes being on opposite-strands. The duplicated region on CTC was manualy deleted in VScode and gene label was changed APC_3UTR.

chr11:108239720-108239839 overlap was between ATM(gene of interest) and C11orf65. The overlap was due to the genes being on opposite-strands. The duplicated region on C11orf65 was manualy deleted in VScode and gene label was changed ATM_3UTR.

chr15:33010462-33010561 overlap was between GREM1(gene of interest) and RP11. The overlap was due to the genes being on opposite-strands. The duplicated region on RP11 was manualy deleted in VScode and gene label was changed GREM1_SCG5_13.

chr15:33010635-33010953 overlap was between GREM1(gene of interest) and RP11. The overlap was due to the genes being on opposite-strands. The duplicated region on RP11 was manualy deleted in VScode and gene label was changed GREM1_SCG5_14.

chr17:56431028-56431147 overlap was between RNF43(gene of interest) and BZRAP1-AS1. The overlap was due to the genes being on opposite-strands. The duplicated region on BZRAP1-AS1 was manualy deleted in VScode and gene label was changed RNF43_3UTR.

chr19:1228320-1228439 overlap was between STK11(gene of interest) and C19orf26. The overlap was due to the genes being on opposite-strands. The duplicated region on C19orf26 was manualy deleted in VScode and gene label was changed STK11_3UTR.
