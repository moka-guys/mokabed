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

### merging parts 2 and 3
Add regions from part 3 not included in part 2

`bedtools subtract -a 'Pan4278_part3data.bed' -b 'Pan4278_part2data.bed' >> 'Pan4278_part2data.bed'`

#### repeat for sambamba
`bedtools subtract -a 'Pan4278_part3dataSambamba.bed' -b 'Pan4278_part2dataSambamba.bed' >> 'Pan4278_part2dataSambamba.bed'`

Part3 BED files are deleted
`rm Pan4278_part3data*`

### merging parts 1 and 2
Add regions from part 2 not included in part 1

`bedtools subtract -a 'Pan4278_part2data.bed' -b 'Pan4278_part1data.bed' >> 'Pan4278_part1data.bed'`

#### repeat for sambamba
`bedtools subtract -a 'Pan4278_part2dataSambamba.bed' -b 'Pan4278_part1dataSambamba.bed' >> 'Pan4278_part1dataSambamba.bed'`

Part2 BED files are deleted
`rm Pan4278_part2data*`

### combining genes with 5' UTR
#### data.bed
The TH gene also includes the 5' UTR. This gene was not included in parts 1-4 so can be concatenated onto the end.
`cat /home/aled/Documents/201229_mokabed/mokabed/LiveBedfiles/Pan4278_THdata.bed >> home/aled/Documents/201229_mokabed/mokabed/LiveBedfiles/Pan4278_part1data.bed`
The header was removed manually
#### sambamba.bed
repeat for sambamba
`cat Pan4278_THdataSambamba.bed >> Pan4278_part1dataSambamba.bed`
There is no header to remove

#### remove TH files
`rm Pan4278_THdata*`

### adding MAPT
The MAPT gene was requested to have 25bp padding, as opposed to 10bp for the rest of the transcripts. There is also 2 transcripts for MAPT which will need combining before adding to the other main file.
#### Add regions from part 2 not included in part 1
The below BED tools subtract command showed there are no differences between the two files
`bedtools subtract -a 'Pan4278_MAPT_part2data.bed' -b Pan4278_MAPT_part1data.bed`

Therefore, just one BED file needs to be combined with Pan4278_part1 files

### Add MAPT to part1data.bed
`cat Pan4278_MAPT_part1data.bed >> Pan4278_part1data.bed `
The header was removed manually (as was the header from the TH step, where the file was not saved after changing)

### Add MAPT to part1dataSambamba.bed
`cat Pan4278_MAPT_part1dataSambamba.bed >> Pan4278_part1dataSambamba.bed `
There was no header to delete

#### remove MAPT bed files
`rm Pan4278_MAPT_part1d*`
`rm Pan4278_MAPT_part2d*`

## problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which was causing mokabed to fail on a previous iteration of this BED file (Pan4278).
Mokabed was failing because cruzdb was returning multiple records for the same transcript.

As described in Pan3937_log.md a number of steps were performed to extract the regions from the UCSC table browser, remove the UTRs, pad by 10 bases and convert to the expected format (12 columns)

This was done for both data.bed and sambamba.bed and were saved as Pan4278_problemdataSambamba.bed and Pan4278_problemdata.bed. These two files were downloaded from the git history at commit 982b443698 (https://github.com/moka-guys/mokabed/tree/982b443698683532c2a4a0032e0ae370742ad41a/LiveBedfiles)

### add to data.bed
`cat Pan4278_problemdata.bed >> Pan4278_part1data.bed`
There was no header to remove

### add to sambamba.bed
`cat Pan4278_problemdataSambamba.bed.txt >> Pan4278_part1dataSambamba.bed`
There was no header to remove

### remove Pan4278 problematic beds"
`rm Pan4278_problemdata*`

## Add intronic SNV sites
We need to add in Pan4284, v2 of the intronic SNVs (padded to 10bp)
This file was not in master when this branch was created so master has been merged into this branch

### add to data.bed
`cat Pan4284.bed >> Pan4278_part1data.bed`

### add to sambamba.bed
`cat Pan4284.bed >> Pan4278_part1dataSambamba.bed `

### fix sambamba bed format
sambamba bed file was modified manually into the correct format

## sort files
`sort Pan4278_part1data.bed -k1,1V -k2,2n -k3,3n > Pan4278_part1data_sorted.bed; mv Pan4278_part1data.bed Pan4278_part1data_unsorted.bed; mv Pan4278_part1data_sorted.bed Pan4278_part1data.bed; rm Pan4278_part1data_unsorted.bed`
header was moved to the top.

## sort sambamba bed file.
`sort Pan4278_part1dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4278_part1dataSambamba_sorted.bed; mv Pan4278_part1dataSambamba.bed Pan4278_part1dataSambamba_unsorted.bed; mv Pan4278_part1dataSambamba_sorted.bed Pan4278_part1dataSambamba.bed; rm Pan4278_part1dataSambamba_unsorted.bed`
no header to move

## rename files
`mv Pan4278_part1data.bed Pan4278data.bed`
`mv Pan4278_part1dataSambamba.bed Pan4278dataSambamba.bed`

## correct whitespace issue in sambamba bed
Done manually, searching for space and converted to tabs

## fix mistake in Pan4284
Pan4284 was found to be incorrect. these changes were reproduced in the two Pan4278 bed files
### sambamba.bed
original
X	149831323	1498313234	X-149831323-1498313234	0	+	MTM1;NM_000252_c.1468-577	4534
corrected
X	149831323	149831334	X-149831323-149831334	0	+	MTM1;NM_000252_c.1468-577	4534

### data.bed
original
X	149831323	1498313234	MTM1_NM_000252_c.1468-577
corrected
X	149831323	149831334	MTM1_NM_000252_c.1468-577

## Testing statement
Both data.bed and dataSambamba.bed have been tested using moka_picard and chanjo_sambamba_v1.10 in 003_210126_Pan4278