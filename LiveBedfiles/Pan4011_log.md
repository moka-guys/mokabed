# Pan4011
This BED file is a replacement of Pan3613 as a component of Pan3613 (Pan3612) was found to contain errors.

Please refer to Pan3613_LogFile.txt for a trail for how these files were created.

## create copies of Pan3613
```
cp /home/aled/Documents/mokabed/LiveBedfiles/Pan3613data.bed /home/aled/Documents/mokabed/LiveBedfiles/Pan4011data.bed
cp /home/aled/Documents/mokabed/LiveBedfiles/Pan3613dataSambamba.bed /home/aled/Documents/mokabed/LiveBedfiles/Pan4011dataSambamba.bed
```

## manually change chromosome 23 to chromosome X
Pan3612 contained 3 positions labeled as chromosome 23 instead of chromosome X.
These were manually corrected in Pan4011data.bed and Pan4011dataSambamba.bed

## sort Pan4011data.bed
sort the bed file.
`sort Pan4011data.bed -k1,1V -k2,2n -k3,3n > Pan4011data_sorted.bed; mv Pan4011data.bed Pan4011data_unsorted.bed; mv Pan4011data_sorted.bed Pan4011data.bed; rm Pan4011data_unsorted.bed`

The header was moved back to the top manually

## sort Pan4011dataSambamba.bed
sort the bed file.
`sort Pan4011dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4011dataSambamba_sorted.bed; mv Pan4011dataSambamba.bed Pan4011dataSambamba_unsorted.bed; mv Pan4011dataSambamba_sorted.bed Pan4011dataSambamba.bed; rm Pan4011dataSambamba_unsorted.bed`

## testing
Both BED files have been tested and worked without error.

## add rs2217652
It was noticed this SNP was missing from Pan4003. Added manually.

Both BED files have been tested and worked without error.

## Pan4011_flat.bed
The varscan and lofreq variant callers require flattened bedfiles, as any variants called within overlapping regions are called once for each region.
This bedfile was created using the command:
`cut -f1-3 /home/aled/Documents/mokabed/LiveBedfiles/Pan4011data.bed | bedtools merge -i - > /home/aled/Documents/mokabed/LiveBedfiles/Pan4011data_flat.bed`