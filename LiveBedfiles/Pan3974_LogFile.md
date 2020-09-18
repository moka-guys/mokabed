# Pan3974
Bioinformaticians were involved in curating the list of transcripts for this gene panel, and at this point the transcripts were not available in Moka.
The list of transcripts is provided in LiveBedFiles/Pan3973 VCP3_Variant_v3.1.txt (Pan3973 is the variant BED file)
This was used to create LiveBedfiles/Transcripts/Pantranscriptfiles/Pan3973.txt - the format required by MokaBED and split into four seperate files (Pan3973_part1.txt,Pan3973_part2.txt etc )to ensure there are not duplicate transcripts for the same gene.
Copies of these files were created and named Pan3974

## problematic transcript
When creating Pan3973 it was found the SMN1 gene returns two records for the same transcripts which caused mokabed to fail. This transcript was excluded from this list and will be created manually.

## Run mokabed on Pan3973_part1-4.txt
These files were manually curated, ensuring there were no duplicate transcripts for each gene. A check was also performed for duplicate transcripts.

All 4 files were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below. 
```
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part1data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part1_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part2data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part2_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part3data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part3_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part4data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part4_LogFile.txt 
```

## Combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part4data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed'`

Adding regions from part4 to part3 does not include any additional regions.

Part4 BED files are deleted

### merging parts 2 and 3
Add regions from part 3 not included in part 2

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2data.bed'`

#### repeat for parts 2 and 3 sambamba
`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3dataSambamba.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2dataSambamba.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2dataSambamba.bed'`

Part3 BED files are deleted