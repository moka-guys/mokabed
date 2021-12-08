# Pan4761
This BED file is used to contain intronic regions to be added into the TSO500 BED file (eg Pan4709)
As per the bedfile request formm this includes 3 regions.
## MET
2 intronic regions of MET (between exons 13+14 and 14+15) - these regions were obtained by looking the genomic coordinates produced by running MokaBED on the transcript and filling the gaps between the padded exons.
## TERT
A single variant in the promotor region (5: 1295228) padded by 5bp

## formatting
An empty line is at the bottom of the file so any potential concatenation of files will ensure they go onto a newline.
Tabs are used to seperate.

## testing
The bedfile was checked in UCSC