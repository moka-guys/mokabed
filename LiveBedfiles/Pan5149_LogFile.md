This BED file is a remake of Pan4995, the VCP3 +/-30bp panel, but with the UTRs padded by +/-30bp

From past attempts of making this BED file there are additional steps required to create this BED file:
    1) SNORD118 gene is non-coding RNA, so doesn't have a NM number. Therefore must be added manually.
    2) LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected.
    3) SMN1 was found to be problematic therefore has to be done manually.
    4) Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database. Both transcripts were compared and no differences were found.

    


