# genepred2exomedepth
This script takes a refseq file and will convert it into a format that can be used by exome depth.

There are 2 inputs, a refseq file and a integer, to pad the regions.
One row is returned for each exon.
The strand is used to create a unique exon name (in format genesymbol_exoncount).

## RefSeq file
Please ensure the refseq file used is accurate, as in some cases this file was not updated if multiple transcripts were used.
Also note the refseq file produced by mokabed is already padded.

A snapshot of refseq file is:
```
#bin	name	chrom	strand	txStart	txEnd	cdsStart	cdsEnd	exonCount	exonStarts	exonSEnds	score	name2	cdsStartStat	cdsEndStat	exonFrames
4595	MUTYH;NM_001128425.2	1	-	45794927	45806162	45794927	45806162	16	45794927,45796137,45796803,45797041,45797282,45797644,45797787,45798012,45798195,45798384,45798539,45798718,45798906,45799034,45800012,45805840	45795159,45796279,45797056,45797278,45797571,45797808,45798032,45798210,45798409,45798556,45798681,45798892,45799046,45799325,45800233,45806162	nan	MUTYH	nan	nan	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```

## Usage
./genepred2exomedepth.sh path/to/REFSEQ/file PADDING(int)

Note the header line may need to be removed