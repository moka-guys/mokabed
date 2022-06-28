# Pan4995
This BED file describes the regions to be assessed (QC, coverage and variant filtering) for SNV variant calling on the VCP3 capture panel which has been updated In June 2022 to meet the changing test directory.

This BED file will be a modification to the existing VCP3 BED file, Pan4535. Pan4535 is the result of a few iterations and improvements from Pan4278 -> Pan4361 (corrected mapping of small exons in LAMA1,DIAPH1 and NBEA) and Pan4361 -> Pan4535 (addition of SNORD118 RNA).

This update includes a number of extra genes which have been added (see Pan4995_extras.txt) and a subset of genes that are already on the panel, but have some extra capture baits added to target promotor regions. These will be added with 5' UTRs padded by 10bp and only regions not already in Pan4535 will be incorporated (see Pan4995_extras_UTRs.txt)