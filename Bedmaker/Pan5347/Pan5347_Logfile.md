## Pan5347
CP205 Whole Capture BED file (build37) for coverage and variant calling

This BEDfile replaces Pan5346; during validation, Michael Mitchel asked to add these 4 5' UTR regions into small variant bed files. Michael Yau asked to remove a region in DMD gene, therefore BEDfiles need to be remade.

The following changes were done in existing Pan5346 databed and sambamba bed files. Since the Pannumber of the bed files need updating, the changes done on existing Pan5346 were copied to a new branch "Pan5347"

## manual adding for 5UTR regions to data bed
Michael Mitchel asked to add these 4 regions into small variant bed files
chr2    128175862    128176040  PROC  
chr3 93692632  93692783   PROS1
chr1        173886443        173886568     SERPINC1   
chr10    27389341     27389395  ANKRD26

These regions were manually added into Pan5346_data.bed

## sorting data bed file
sort -k1,1V -k2,2n Pan5346_data.bed -o Pan5346_data.bed

## remove a DMD region
The following region was removed from data bed as requested by Michael Yau
DMD NM_000109.4 2928 X 32489312 32489322 

## manual adding for 5UTR regions to sambamba bed
Michael Mitchel asked to add these 4 regions into small variant bed files
chr2    128175862    128176040  PROC  
chr3 93692632  93692783   PROS1
chr1        173886443        173886568     SERPINC1   
chr10    27389341     27389395  ANKRD26

These regions were manually added into Pan5346_sambamba.bed

## sorting sambamba bed
sort -k1,1V -k2,2n Pan5346_sambamba.bed -o Pan5346_sambamba.bed

## remove a DMD region from sambamba bed
The following region was removed from sambamba bed as requested by Michael Yau
DMD NM_000109.4 2928 X 32489312 32489322 

## testing
updated data bed and sambamba bed were testing by running filtering app and coverage app on DNAnexus.
The apps finished without error. 

After copying all above changes Pan5346 bedfiles were renamed as Pan5347.

# Rename the bed file
mv Pan5346_data.bed Pan5347_data.bed
mv Pan5346_sambamba.bed Pan5347_sambamba.bed 

## testing
Renamed bed file were tested again by running filtering app and coverage app on DNAnexus.
The apps finished without error. 