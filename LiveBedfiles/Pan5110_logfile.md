# Pan5110 logfile
This BED file contains the coding regions (+/-10bp) for all 523 genes included in the TSO500 capture. It has been made to allow coverage reports to be generated for all genes, sometimes required for adhoc requests from clinicians to analyse genes not included in national genomic test directory panels.
The TSO500 gene list was checked to ensure gene symbols are up to date using the Ensembl biomart tool. 32 genes had out of date gene symbols. The BED file request form includes the gene name on the Illumina list and the HGNC gene symbol.
Transcript selection used MANE select and MANE plus clinical transcripts for most (521 genes). Two remaining genes to be added separately, RUNX1T1 and TERC. 
TERT promoter regions are also included, taken from Pan4968.

## Transcript and gene list files
Two transcript list files created (transcripts 2 contains second transcripts for 10 genes, mostly MANE plus clinical).
A gene list for, Pan5110_genelist.txt created to use running mokabed with gene symbols for RUNX1T1 because a specific transcript could not be identified.

The transcript lists were created using the original list from Illumina, and using ensembl biomart to check gene symbols and identify MANE transcripts. Total number of genes = 523 at all stages.