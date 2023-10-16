This VCP3 BED file is a remake of Pan5149, but with no padding to the exons and only the 5 UTR included.

From past attempts of making this BED file there are additional steps required to create this BED file: 
    - SNORD118 gene is non-coding RNA, so doesn't have a NM number. Therefore must be added manually.
    - LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected.
    - SMN1 was found to be problematic therefore has to be done manually.
    - Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database. Both transcripts were compared and no differences were found.

