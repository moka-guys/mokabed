# Pan3794
Bioinformaticians were involved in curating the list of transcripts for this gene panel, and at this point the transcripts were not available in Moka.
The list of transcripts is provided in LiveBedFiles/Pan3973 VCP3_Variant_v3.1.txt (Pan3973 is the variant BED file)
This was used to create LiveBedfiles/Transcripts/Pantranscriptfiles/Pan3973.txt - the format required by MokaBED and split into four seperate files (Pan3973_part1.txt,Pan3973_part2.txt etc )to ensure there are not duplicate transcripts for the same gene.
Copies of these files were created and named Pan3974

## problematic transcript
When creating Pan3973 it was found the SMN1 gene returns two records for the same transcripts which caused mokabed to fail. This transcript was excluded from this list and will be created manually.