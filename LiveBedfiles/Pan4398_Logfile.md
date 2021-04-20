# Pan4398
This BED file is used to restict variant calling for the VCP1 Panel. This was previously created in Pan4302, but a mistake was found in the mapping of one of the LAMA2 exons. Therefore, a copy of those files were made and manually edited.

The incorrect coordinates are:
incorrect coordinates - chr6:129763337-129763402
correct coordinates - chr6:129764177-129764243


## take copies of Pan4302data.bed and Pan4302dataSambamba.bed
`cp Pan4302data.bed Pan4398data.bed`
`cp Pan4302dataSambamba.bed Pan4398dataSambamba.bed`

## edit data.bed
This line was changed 
6	129763336	129763402	3908										LAMA2;NM_000426.4
to
6	129764177	129764243	3908										LAMA2;NM_000426.4

## edit datasambamba.bed
6	129763336	129763402	6-129763336-129763402	0	+	LAMA2;NM_000426.4	3908
was changed to
6	129764177	129764243	6-129764177-129764243	0	+	LAMA2;NM_000426.4	3908

## testing
These BED files were tested using Mokapicard_v1.1, gatk human exome pipeline v1.5 and chanjo_sambamba_v1.6. All jobs completed without error