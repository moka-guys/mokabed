# Pan4361
This BED file is used for the VCP3 panel to calculate coverage and to restrict variant calling.
Errors were noticed where small exons had been mapped incorrectly in the UCSC refseq database. This means that variant calling and coverage calculations were performed on different regions that were taregetted by the capture kit.

Three areas were identified:
LAMA2:
incorrect coordinates - chr6:129763357-129763382
correct coordinates - chr6:129764197-129764223

DIAPH1:
incorrect coordinates - chr5:140915611-140915639
correct coordinates - chr5:140950984-140951013

NBEA
incorrect coordinates - chr13:35739221-35739245
correct coordinates - chr13:35743113-35743142

These BED files will be based on copies of Pan4278.
 
 ## take copies of Pan4278data.bed and Pan4278dataSambamba.bed
cp Pan4278data.bed Pan4361data.bed
cp Pan4278dataSambamba.bed Pan4361dataSambamba.bed

## edit Pan4631data.bed
The three regions were changed manually after double checking with the genome browser for correct padding and that coordinates are zero based, open ended.
for clarity the changed lines are:

old - 6	129763356	129763382	3908										LAMA2;NM_000426.4
new - 6	129764197	129764223	3908										LAMA2;NM_000426.4

old - 5	140915610	140915639	1729										DIAPH1;NM_005219.5
new - 5	140950984	140951013	1729										DIAPH1;NM_005219.5

old - 13	35739220	35739245	26960										NBEA;NM_015678.5
new - 13	35743113	35743142	26960										NBEA;NM_015678.5

## edit Pan4631dataSambamba.bed
The three regions were changed manually in the sambamba BED file:

old - 6	129763356	129763382	6-129763356-129763382	0	+	LAMA2;NM_000426.4	3908
new - 6	129764197	129764223	6-129764197-129764223	0	+	LAMA2;NM_000426.4	3908

old - 5	140915610	140915639	5-140915610-140915639	0	+	DIAPH1;NM_005219.5	1729
new - 5	140950984	140951013	5-140950984-140951013	0	+	DIAPH1;NM_005219.5	1729

old - 13	35739220	35739245	13-35739220-35739245	0	+	NBEA;NM_015678.5	26960
new - 13	35743113	35743142	13-35743113-35743142	0	+	NBEA;NM_015678.5	26960

## Testing
Both bed files have been tested - jobs completed without error.