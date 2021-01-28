# Pan4278
This BED file is for use with coverage and variant calling with the VCP3 capture panel.

The complete transcript list can be found in Pan4278.txt

In general there are a number challenges when making this BED file:
1. Genes with multiple transcripts - these must be combined without duplicating regions, using bedtools subtract. To allow for this the transcript list (the mokaBED input) was split into 4 files (Pan4278_part1-4.txt), ensuring there was only a single transcript for each gene in each file and MokaBED run for each file.
2. There are other genes which either requires a different amount of padding or inclusion of the 5' UTRs. Again, MokaBED was run for each scenario and these will be concatenated into the main file.
3. From previous attempts to make this file (Pan4278) one transcript was found to cause a problem (SMN1) so will again be done manually.

## Combining multiple transcripts
### parts 4 and 3
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:
`bedtools subtract -a Pan4278_part4data.bed -b Pan4278_part3data.bed >> Pan4278_part3data.bed`
Adding regions from part4 to part3 does not include any additional regions.

Part4 BED files are deleted
`rm Pan4278_part4data*`