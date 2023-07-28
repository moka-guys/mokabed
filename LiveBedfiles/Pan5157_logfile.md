# Pan5157
This BEDfile is a subset of Pan3610 that is specific to R430. 
These regions were provided by Michael Yau and Lorraine Hawkes when requesting a BEDfile for the R430 exome depth CNV filtering stage.


## Take a copy of Pan3610
`cp Pan3610.bed Pan5157.bed`

## manually remove unwanted regions
This was performed manually. There are 16 rows, matching the request form and the coordinates were checked. There is an empty new line at the end.

WARNING.
NOTE THIS BEDFILE INCORRECTLY CONTAINS RAD51D. USE OF THIS BEDFILE COULD RESULT IN CNVS OVERLAPPING WITH THIS REGION BEING INCORRECTLY INCLUDED IN A REPORT. PLEASE USE PAN5164 INSTEAD