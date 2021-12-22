# Pan4841
This BED file is used to calculate coverage for the TSO500 panel.
It consists of ~60 genes (a subset of the 500+ genes on the panel).
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.
This file is the same as Pan4709 but with the UTRs removed

## Request form Pan4841.csv
The Pan4709.csv form was copied and edited to remove UTRs.

## Transcript files
Four transcript files were created for Pan4709 (Pan4709_part1-4.txt). These files were manually curated, ensuring there were no duplicate transcripts for each gene. A check was also performed for duplicate transcripts. They were copied Pan4841_part1-4.txt (cp Pan4709_part1.txt Pan4841_part1.txt)

## Run mokabed
All 4 sets of transcripts were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below.

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4841_part1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4841_part1data.bed --logfile /home/dnanexus/out/Output_files/Pan4841_part1_LogFile.txt `

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4841_part2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4841_part2data.bed --logfile /home/dnanexus/out/Output_files/Pan4841_part2_LogFile.txt `

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4841_part3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4841_part3data.bed --logfile /home/dnanexus/out/Output_files/Pan4841_part3_LogFile.txt `

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4841_part4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4841_part4data.bed --logfile /home/dnanexus/out/Output_files/Pan4841_part4_LogFile.txt `

## combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

### parts 3 and 4
`bedtools subtract -a 'Pan4841_part4data.bed' -b 'Pan4841_part3data.bed' >> Pan4841_part3data.bed`
This resulted in no additonal regions being added.

Part 4 BED files were deleted
`rm Pan4841_part4data*`

*at this stage realised that sambamba.bed files were not included so downloaded all then deleted part4dataSambamba.bed*

### parts 2 and 3
Add regions from part 3 not in part 2 for data.bed and sambamba.bed
`bedtools subtract -a 'Pan4841_part3data.bed' -b 'Pan4841_part2data.bed' >> Pan4841_part2data.bed`
`bedtools subtract -a 'Pan4841_part3dataSambamba.bed' -b 'Pan4841_part2dataSambamba.bed' >> Pan4841_part2dataSambamba.bed`

Remove part 3
`rm Pan4841_part3data*`

### parts 1 & 2
Add regions from part 2 not in part 1 for data.bed and sambamba.bed
`bedtools subtract -a 'Pan4841_part2data.bed' -b 'Pan4841_part1data.bed' >> Pan4841_part1data.bed`
`bedtools subtract -a 'Pan4841_part2dataSambamba.bed' -b 'Pan4841_part1dataSambamba.bed' >> Pan4841_part1dataSambamba.bed`

remove part2 files
`rm Pan4841_part2data*`

## Add intronic regions
concatenate intronic regions (Pan4761) into data.bed
`cat Pan4761.bed >> Pan4841_part1data.bed `

manually modify the intronic regions to match data.bed format (EntrezID taken from other MET regions, or from Pan4709 for TERT)