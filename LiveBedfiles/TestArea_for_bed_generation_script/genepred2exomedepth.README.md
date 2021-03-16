# genepred2exomedepth
This script takes a refseq file and will convert it into a format that can be used by exome depth.

There are 2 inputs, a refseq file and a integer, to pad the regions.
One row is returned for each exon.
The strand is used to create a unique exon name (in format genesymbol_exoncount).

# refseq file
Please ensure the refseq file used is accurate, as in some cases this file was not updated if multiple transcripts were used.
Also note the refseq file produced by mokabed is already padded.

## usage
./genepred2exomedepth.sh path/to/REFSEQ/file PADDING(int)

Note the header line may need to be removed