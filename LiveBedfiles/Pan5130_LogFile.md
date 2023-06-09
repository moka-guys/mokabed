# Pan4969 logfile
This BED file is used to calculate coverage for the TSO500 panel.
It consists of a subset of the 500+ genes on the panel, which are used for clinical reporting.
MANE select and MANEplusClinical transcripts for all genes have been selected.
Non coding regions from Pan4968 will be added.
This new version of the TSO500 coverage bedfile contains different genes from the previous bed file (Pan4969), some removed, others added, and therefore will replace the previous bed file.

## Transcript files
Two transcript files were generated based on the transcripts in the request form. The transcripts were identified using ensembl Biomart, providing the HGNC gene symbol and returning MANE and MANEplusClinical transcript lists
Files reformated with amended headers to match format required by mokabed. Accession added as 0 as will not be used by script anyway. The transcript files were checked by comparing the genes in the biomart output with the original list to ensure no genes were missed. Some of the gene symbols provided were out of date; the HGNC gene symbol was identified from the ensembl and HGNC websites and included in the list (TCEB1 is now ELOC and FAM123B is now AMER1). The files were also visually inspected to check for duplicates and errors. 
