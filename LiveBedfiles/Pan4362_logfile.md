# Pan4362
This BED file is used for RPKM on VCP3 panel.
Errors were noticed in Pan3974 where small exons had been mapped incorrectly in the UCSC refseq database. This means that the regions used for read depth/RPKM calculations were different regions than the regions targetted by the capture kit.

Three areas were identified (only padded +/-10bp):
LAMA2:
incorrect coordinates - chr6:129763357-129763382
correct coordinates - chr6:129764197-129764223

DIAPH1:
incorrect coordinates - chr5:140915611-140915639
correct coordinates - chr5:140950984-140951013

NBEA
incorrect coordinates - chr13:35739221-35739245
correct coordinates - chr13:35743113-35743142

These BED files will be based on copies of Pan3974.

## create copy of RPKM BED file
cp Pan3974_RPKM.bed Pan4362_RPKM.bed

## manually edit lines
DIAPH1 was changed from
5	140915570	140915679	1729
to
5	140950944	140951053	1729

LAMA2 was changed from
6	129763316	129763422	3908
to
6	129764157	129764263	3908

NBEA was changed from
13	35739180	35739285	26960
to
13	35743073	35743182	26960

## Testing
The BED file have been tested - job completed without error.