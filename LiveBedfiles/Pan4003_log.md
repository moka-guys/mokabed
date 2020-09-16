# Pan4003
It was noticed that Pan3612 was made incorrectly, with chromsome X incorrectly being labelled chr 23.
Pan3623 includes Pan3612 therefore Pan3623 must be retired and recreated 
NB please see Pan3623_LogFile.txt for full instructions how Pan3623.bed was created

## create copies of the files
```
cp '/home/aled/Documents/mokabed/LiveBedfiles/Pan3623data.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan4003data.bed' 
cp '/home/aled/Documents/mokabed/LiveBedfiles/Pan3623dataSambamba.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan4003dataSambamba.bed' 
```

## manually correct
chromosome 23 was replaced by chromosome X manually in both files (3 locations in each file)

## sort Pan4003data.bed
sort the bed file.
`sort Pan4003data.bed -k1,1V -k2,2n -k3,3n > Pan4003datasorted.bed ; mv Pan4003data.bed Pan4003data_unsorted.bed; mv Pan4003datasorted.bed Pan4003data.bed; rm Pan4003data_unsorted.bed`

The header was moved back to the top manually