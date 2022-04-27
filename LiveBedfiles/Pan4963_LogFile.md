# Pan4963
This BED file is used to calculate coverage for the TSO500 panel.
It consists of ~60 genes (a subset of the 500+ genes on the panel).
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.
This file is the same as Pan4841 but with the TERT promoter regions changed

## Request form
The Pan4841.csv form was copied and edited to include the TERT promoter regions as discussed with the cancer team.

## copy Pan4841 files
`cp Pan4841data.bed Pan4963data.bed`
`cp Pan4841dataSambamba.bed Pan4963dataSambamba.bed`

## add correct TERT promoter regions to data.bed
Correct TERT promoter regions added and incorrect region deleted from Pan4963data.bed (manually).

## add correct TERT promoter regions to dataSambamba.bed
Correct TERT promoter regions added and incorrect region deleted from Pan4963dataSambamba.bed (manually).

## sort bed files
### sort Pan4963data.bed
`mv Pan4963data.bed Pan4963data_unsorted.bed; sort Pan4963data_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4963data.bed; rm Pan4963data_unsorted.bed`

### sort Pan4962dataSambamba.bed
`mv Pan4963dataSambamba.bed Pan4963dataSambamba_unsorted.bed; sort Pan4963dataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4963dataSambamba.bed; rm Pan4963dataSambamba_unsorted.bed`

## move header
manually moved header of Pan4963data.bed back to top

## Testing
tested Pan4963dataSambamba.bed with HD200 sample from TSO22014 running chanjo_sambamba_coverage_v1.13 applet. App failed

## replace spaces with tabs
Some fields were separated with spaces not tabs, which may have caused the testing to fail.

## Further testing
tested Pan4963dataSambamba.bed with HD200 sample from TSO22014 running chanjo_sambamba_coverage_v1.13 applet. 