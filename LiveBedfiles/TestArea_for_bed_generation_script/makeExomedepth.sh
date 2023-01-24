#!/bin/sh

# Creates meta-exons (flattened coding exons) for a capture region
# Usage:
#	makeExomedepth.sh hg19 output capture.bed extras.bed
#
# NB The extras.bed command allows to add extra regions after the capture filtering process (eg to patch in some exons not in UCSC)
#    Missed capture regions not intersecting the exon set will be highlighted in the end.

ORG=$1
OUTPUT=$2
CAPTURE=$3
EXTRA=$4
REFGENE=${OUTPUT}.genepred
BED12=${OUTPUT}'.bed'
TXEXONS=${OUTPUT}'.txexons.bed'
CDSEXONS=${OUTPUT}'_cdsexons.bed'
CAPTUREEXONS=${OUTPUT}'_captureexons.bed'
CAPTUREEXONSCORRECTED=${OUTPUT}'_captureexonscorrected.bed'
METAEXONS=${OUTPUT}'_metaexons.bed'
EXOMEDEPTH=${OUTPUT}'_exomedepth.bed'
MISSED=${OUTPUT}'_missed.bed'
UCSCENSEMBL=${OUTPUT}'.chromosomes'
BEDSORT=sort

# 1 r.bin, 2 r.name, 3 r.chrom, 4 r.strand, 5 r.txStart, 6 r.txEnd, 7 r.cdsStart, 8 r.cdsEnd, 9 r.exonCount,
# 10 r.exonStarts, 11 r.exonEnds, 12 r.score, 13 r.name2, 14 r.cdsStartStat, 15 r.cdsEndStat, 16 r.exonFrames

if [ ! -s ${REFGENE} ]; then
	echo "Getting refGene table..."
	mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -N -D $ORG -P 3306 \
	 -e 'SELECT r.bin,CONCAT(r.name,".",i.version),r.chrom,r.strand,r.txStart,r.txEnd,
	r.cdsStart,r.cdsEnd,r.exonCount,r.exonStarts,r.exonEnds,r.score,r.name2,
	r.cdsStartStat,r.cdsEndStat,r.exonFrames from refGene as r, hgFixed.gbCdnaInfo as i WHERE r.name=i.acc AND r.name LIKE "NM_%" ORDER BY r.bin;' > ${REFGENE}.${ORG}
	
	# get hg/GRCh conversion
	echo "Getting UCSC->Ensembl chromosome table..."
	mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -N -D $ORG -P 3306 \
	 -e "select c.ucsc,c.ensembl,i.size from chromInfo as i, ucscToEnsembl as c where c.ucsc = i.chrom;" > ${UCSCENSEMBL}
	# -A disables autocompletion rehashing, -N disables column name output (to get a clean output)
	
	## convert to UCSC chromosome names
	echo "Converting refGene table to GRCh chromosome names..."
	awk 'BEGIN { OFS = "\t" };
	{
	  if (NR == FNR) {
	    chrom[$1] = $2
	  }
	  else {
	    $3=chrom[$3]
	    print $0
	  }
	}
	' ${UCSCENSEMBL} ${REFGENE}.${ORG} > ${REFGENE}
fi


# create refGene BED files from ${REFGENE}
echo "Building refGene BED12..."
awk '
BEGIN { OFS = "\t" };
{
  delete astarts;
  delete aends;
  split($10, astarts, /,/);
  split($11, aends, /,/);
  starts="";
  sizes="";
  exonCount=0;
  for(i=1; i in astarts; i++){
      if (! astarts[i]) continue
      sizes=sizes""(aends[i] - astarts[i])","
      starts=starts""(astarts[i] = astarts[i] - $5)","
      exonCount=exonCount + 1
  }
  print $3,$5,$6,$2,$12,$4,$7,$8,"0",exonCount,sizes,starts
}
' ${REFGENE} | ${BEDSORT}  -k1,1 -k2n,3n > ${BED12}

# BED exon files with symbols
echo "Building CDS exons..."
awk '
BEGIN { OFS = "\t" };
{
  delete astarts;
  delete aends;
  split($10, astarts, /,/);
  split($11, aends, /,/);
  starts=""
  sizes=""
  exonCount=0
  for(i=1; i in astarts; i++){
    if (! astarts[i]) continue
    if (aends[i]<$7) continue
    if (astarts[i]>$8) continue
    print $3,(astarts[i] < $7 ? $7 : astarts[i]),($8 < aends[i] ? $8 : aends[i]),$13,$12,$4
  }
}
' ${REFGENE} | ${BEDSORT} -k1,1 -k2n,3n > ${CDSEXONS}

# BED transcript exons file
echo "Building RefSeq Transcript Exons..."
awk 'BEGIN { OFS = "\t" };
{
  delete astarts;
  delete aends;
  split($10, astarts, /,/);
  split($11, aends, /,/);
  starts=""
  sizes=""
  exonCount=0
  for(i=1; i in astarts; i++){
    if (! astarts[i]) continue
    print $3,astarts[i],aends[i],($4 == "-" ? $2"-"length(astarts)-i : $2"-"i),$12,$4
  }
}
' ${REFGENE} | ${BEDSORT} -k1,1 -k2n,3n > ${TXEXONS}

# intersect with capture file (get exons with any overlap in a capture region, -u flag)
echo "Intersecting with capture..."
bedtools intersect -u -a ${CDSEXONS} -b ${CAPTURE} > ${CAPTUREEXONS}

# add exons that are misrepresented in UCSC refgene
if [ -s ${EXTRA} ]; then
	echo "Adding extra regions..."
	cat ${CAPTUREEXONS} ${EXTRA} | sort -k1,1 -k2n,3n > ${CAPTUREEXONSCORRECTED}
	mv ${CAPTUREEXONSCORRECTED} ${CAPTUREEXONS}
fi

# merge exons (create meta-exons)
echo "Creating meta-exons..."
bedtools merge -o distinct,sum,distinct -c 4,5,6 -s -i ${CAPTUREEXONS} > ${METAEXONS}

echo "Numbering exons..."
awk '
BEGIN { OFS = "\t" };
NR==FNR {
  EXONCOUNT[$4]+=1
  next
}
{
  EXONITER[$4]+=1
  exonNumber= ($6 == "-") ? (EXONCOUNT[$4]+1-EXONITER[$4]) : EXONITER[$4]
  print $1,$2,$3,$4"_"exonNumber

}
' ${METAEXONS} ${METAEXONS} > ${EXOMEDEPTH}

# write and print any miissed capture regions by subtracting the built exomedepth BED file
echo "Missed capture regions:"
bedtools intersect -v -a ${CAPTURE} -b ${EXOMEDEPTH} | tee ${MISSED}
echo ""

echo "Written output to ${EXOMEDEPTH}"

