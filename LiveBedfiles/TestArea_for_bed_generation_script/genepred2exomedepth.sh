#!/bin/sh
REFGENE=$1
PADDING=$2

# BED files with exon numbers for exomedepth
# Refseq files have one line per gene (see readme for an example refseq line)
# the below loop goes through each line and:
# takes the columns exonStarts and exonSEnds and splits into new lists astarts and aends for each gene
# for each exon the strand is assessed and the exon count is calculated
# if minus strand then the exon numbers are subtracted from exon count, else just take the exon count
# the chromosome, start (minus padding), stop (plus padding) and gene_exonNumber printed to screen

# set file seperation
awk -v padding=${PADDING} '
BEGIN { OFS = "\t" };
{
  delete astarts;
  delete aends;
  split($10, astarts, /,/);
  split($11, aends, /,/);
  exonCount=length(astarts)
  for(i=1; i in astarts; i++){
    if (! astarts[i]) continue
    exonNumber= ($4 == "-") ? (exonCount+1-i) : i
    print $3,astarts[i]-padding,aends[i]+padding,$13"_"exonNumber
  }
}
' ${REFGENE}

