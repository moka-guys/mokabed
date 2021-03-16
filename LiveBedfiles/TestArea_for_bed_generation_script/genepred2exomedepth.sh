#!/bin/sh
REFGENE=$1
PADDING=$2

# BED files with exon numbers for exomedepth
#echo "Building ExomeDepth exons..."
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

