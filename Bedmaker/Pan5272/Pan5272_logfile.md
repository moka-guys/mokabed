# Pan5272
CP2 Whole Capture BED file (build37) for coverage and variant calling.

It is a copy of Pan5232, it was noticed Bedmaker assigned NM transcripts as gene name for certain genes.

# Take a copy data.bed and sambamaba.bed

cp Pan5232_data.bed Pan5272_data.bed

cp Pan5232_sambamba.bed Pan5272_sambamba.bed

# Manual fix
Fix regions with genes names as transcript numbers. E.g NM_016653;NM_016653.2 should be MAP3K20;NM_016653.2

Open Pan5272_data.bed in Excel and seperate out the columns based on ";"
Search the 5th column for any "NM" and replace the transcript ID with gene symbol
The correct gene symbol was obtained from Ensembl by searching for the transcript ID

Join the gene symbol and transcript ID together (MAP3K20;NM_016653.2) using the Concat function. 

Only MAP3K20 and POMK had this issue.

Note: Excel saves in a csv format, open the file in VScode to convert back into tab-seperated (find&replace "," with "\")

