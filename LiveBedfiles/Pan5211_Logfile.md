# Pan5211
This VCP3 BED file is a remake of Pan5192, few requested genes(DOLK,FANCF,NHLRC1,PRKACG,RNF113A,THBD,RNU4ATAC) were found to be missing from Pan5192.

From past attempts of making this BED file there are additional steps required to create this BED file: -
 - SNORD118 and RNU4ATAC genes are non-coding RNA, so don't have a NM number. Therefore must be added manually. 
 - LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected. 
 - SMN1 was found to be problematic therefore has to be done manually.
 - Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database.   Both transcripts were compared and no differences were found.

 # Create Transcript files
For few genes multiple transcript have been requested, these were separated into Pan5211.txt, Pan5211_part1.txt, and Pan5211_part2.txt