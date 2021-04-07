# Pan4361
This BED file is used for the VCP3 panel to calculate coverage and to restrict variant calling.
Errors were noticed where small exons had been mapped incorrectly in the UCSC refseq database. This means that variant calling and coverage calculations were performed on different regions that were taregetted by the capture kit.

Three areas were identified:
LAMA2:
incorrect coordinates - chr6:129763357-129763382
correct coordinates - chr6:129764198-129764223

DIAPH1:
incorrect coordinates - chr5:140915611-140915639
correct coordinates - chr5:140950985-140951013

NBEA
incorrect coordinates - chr13:35739221-35739245
correct coordinates - chr13:35743114-35743142

These BED files will be based on copies of Pan4278.
 
 ## take copies of Pan4278data.bed and Pan4278dataSambamba.bed
cp Pan4278data.bed Pan4361data.bed
cp Pan4278dataSambamba.bed Pan4361dataSambamba.bed