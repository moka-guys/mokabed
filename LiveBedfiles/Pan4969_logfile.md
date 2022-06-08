# Pan4969 logfile
This BED file is used to calculate coverage for the TSO500 panel.
It consists of a subset of the 500+ genes on the panel, which are used for clinical reporting.
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.
This new version of the TSO500 coverage bedfile contains additional genes and therefore will replace the previous bed file (Pan4963).

## Transcript files
There are multiple transcripts for several of the genes request. Four transcript files were created manually to ensure no duplicate transcripts were included. These are saved as Pan4969_transcripts1-4.txt/
Files reformated with amended headers to match format required by mokabed. Accession added as 0 as will not be used by script anyway.
