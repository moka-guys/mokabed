# Pan4709
This BED file is used to calculate coverage for the TSO500 panel.
It consists of ~60 genes (a subset of the 500+ genes on the panel).
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.

## Pan4709_part1-4.txt
These files were manually curated, ensuring there were no duplicate transcripts for each gene. A check was also performed for duplicate transcripts.

All 4 sets of transcripts were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below.
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 0 --down 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4709_part1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4709_part1data.bed --logfile /home/dnanexus/out/Output_files/Pan4709_part1_LogFile.txt `
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 0 --down 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4709_part2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4709_part2data.bed --logfile /home/dnanexus/out/Output_files/Pan4709_part2_LogFile.txt `
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 0 --down 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4709_part3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4709_part3data.bed --logfile /home/dnanexus/out/Output_files/Pan4709_part3_LogFile.txt `
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 0 --down 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4709_part4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4709_part4data.bed --logfile /home/dnanexus/out/Output_files/Pan4709_part4_LogFile.txt `

## combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

`bedtools subtract -a 'Pan4709_part4data.bed' -b 'Pan4709_part3data.bed' >> Pan4709_part3data.bed`

This resulted in no additonal regions being added.

Part 4 BED files were deleted
` rm Pan4709_part4data*`