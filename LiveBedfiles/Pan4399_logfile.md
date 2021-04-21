# Pan4399
This BED file is used to perform RPKM analysis for the VCP1 Panel. This was previously created in Pan3624, but a mistake was found in the mapping of one of the LAMA2 exons. Therefore, a copy of those files were made and manually edited.

The incorrect coordinates are:
incorrect coordinates - chr6:129763316-129763422
correct coordinates - chr6:129764157-129764263


## take copies of Pan3624data.bed and Pan3624_RPKM.bed
`cp Pan3624data.bed Pan4399data.bed`
`cp Pan3624_RPKM.bed Pan4399_RPKM.bed` 

# edit data.bed
This line was changed 
6	129763316	129763422	3908										LAMA2;NM_000426.4
to
6	129764157	129764263	3908										LAMA2;NM_000426.4

## edit RPKM.bed
6	129763316	129763422	3908
was changed to
6	129764157	129764263	3908

## testing
These BED files were tested using Mokapicard_v1.1 and RPKM_using_conifer_v1.6. All jobs completed without error