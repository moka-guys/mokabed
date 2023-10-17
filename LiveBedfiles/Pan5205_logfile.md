# Pan5205 
This bedfile is for TSO500 coverage calculations.
It replaces the previous bedfile Pan5130, and is based on that file.
When Pan5130 was introduced it was noticed that two regions in BRAF were included in the bedfile that are not present in the capture. This results in low coverage which must be checked for every sample requiring BRAF analysis, which adds time to the analysis. The additional regions are exons from the MANEPlusClinical transcript NM_001374258.1:

chr7	140426283	140426326	7-140426283-140426326	0	+	BRAF;NM_001374258.1	673
chr7	140485478	140485618	7-140485478-140485618	0	+	BRAF;NM_001374258.1	673

This new bedfile will be made by deleting the regions from the existing Pan5130.

## Copy original bedfile
`cp Pan5130data.bed Pan5205data.bed`
`cp Pan5130dataSambamba.bed Pan5205dataSambamba.bed`

## Remove regions
manually delete two regions from each bedfile

## Testing
These bed files were tested using sambamba coverage and moka picard apps.

### Sambamba
The sambamba app was run on the HD200 sample from TSO23039 using the original dx run command, modified to use the correct BED file and output to the Pan5205 test project. 
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-G6vyyf00jy1kPkX9PJ1YkxB1 --detach -y --brief --name=TSO23039_01_22069_HD200_Pan5114.bam -ibam_index=project-GZG0ZQ80V707jGbPX3G11QyJ:file-GZGk1zQ0v3v0kXvB2jVJjXG3 -ibamfile=project-GZG0ZQ80V707jGbPX3G11QyJ:file-GZGk1zQ0v3vJK9x64PZ733pb -icoverage_level=100 -isambamba_bed=003_231017_Pan5205:/Pan5205dataSambamba.bed -imerge_overlapping_mate_reads=true -iexclude_failed_quality_control=true -iexclude_duplicate_reads=true -imin_base_qual=25 -imin_mapping_qual=30 --dest=003_231017_Pan5205`

App completed without error

### Picard
The MokaPicard app was previously found to fail with TSO500 bam files, presumed to be due to an issue with the bam. Therefore this bed file was tested with the NA12878 bam file from NGS536B (VCP3). App (v1.2) completed successfully suggesting the bed file is valid.

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-G9yJ57j0jy1ZV0fxPZZXJ8FJ --detach -y --brief --name=NGS582B_NA12878 -iCapture_panel=Hybridisation -isorted_bam=project-GZY76f004PK0ZB86b1YV1k7B:file-GZYQXfj05p4jQ8G37q266v68 -ifasta_index=project-FVpfGp00vgV46F1xJx7y4YJ7:file-ByYgX700b80gf4ZY1GxvF3Jv -ivendor_exome_bedfile=Pan5205data.bed --dest=003_231017_Pan5205`

App completed without error