# Pan4397
This BED file is used to calculate coverage for the VCP1 Panel. This was previously created in Pan4287, but a mistake was found in the mapping of one of the LAMA2 exons. Therefore, a copy of those files were made and manually edited.

The incorrect coordinates are:
incorrect coordinates - chr6:129763357-129763382
correct coordinates - chr6:129764197-129764223


## take copies of Pan4287data.bed and Pan4287dataSambamba.bed
`cp Pan4287data.bed Pan4397data.bed`
`cp Pan4287dataSambamba.bed Pan4397dataSambamba.bed`

# edit data.bed
This line was changed 
6	129763356	129763382	3908										LAMA2;NM_000426.4
to
6	129764197	129764223	3908										LAMA2;NM_000426.4

## edit datasambamba.bed
6	129763356	129763382	6-129763356-129763382	0	+	LAMA2;NM_000426.4	3908
was changed to
6	129764197	129764223	6-129764197-129764223	0	+	LAMA2;NM_000426.4	3908

## testing
These BED files were tested using Mokapicard_v1.1, gatk human exome pipeline v1.5 and chanjo_sambamba_v1.6. All jobs completed without error