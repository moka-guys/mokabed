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

### parts 3 & 4
`bedtools subtract -a 'Pan4709_part4data.bed' -b 'Pan4709_part3data.bed' >> Pan4709_part3data.bed`

This resulted in no additonal regions being added.

Part 4 BED files were deleted
` rm Pan4709_part4data*`

### parts 2 & 3
Add regions from part 3 not in part 2 for data.bed and sambamba.bed
`bedtools subtract -a 'Pan4709_part3data.bed' -b 'Pan4709_part2data.bed' >> Pan4709_part2data.bed`
`bedtools subtract -a 'Pan4709_part3dataSambamba.bed' -b 'Pan4709_part2dataSambamba.bed' >> Pan4709_part2dataSambamba.bed`

Remove part 3
` rm Pan4709_part3data*`

### parts 1 & 2
Add regions from part 2 not in part 1 for data.bed and sambamba.bed
`bedtools subtract -a 'Pan4709_part2data.bed' -b 'Pan4709_part1data.bed' >> Pan4709_part1data.bed`
`bedtools subtract -a 'Pan4709_part2dataSambamba.bed' -b 'Pan4709_part1dataSambamba.bed' >> Pan4709_part1dataSambamba.bed`

remove part2 files
`rm Pan4709_part2data*`

## Add intronic regions
concatenate intronic regions (Pan4761) into data.bed
`cat Pan4761.bed >> Pan4709_part1data.bed `

manually modify the intronic regions to match data.bed format

concatenate intronic regions (Pan4761) into dataSambamba.bed
`cat Pan4761.bed >> Pan4709_part1dataSambamba.bed `

intronic regions edited manually to match sambamba format in Pan4709_part1dataSambamba.bed 

## sort bedfiles
#### data.bed
`mv Pan4709_part1data.bed Pan4709_part1data_unsorted.bed; sort Pan4709_part1data_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4709_part1data.bed; rm Pan4709_part1data_unsorted.bed`
header moved to top manually

#### dataSambamba.bed
`mv Pan4709_part1data.bed Pan4709_part1dataSambamba_unsorted.bed; sort Pan4709_part1dataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4709_part1dataSambamba.bed; rm Pan4709_part1dataSambamba_unsorted.bed`


## rename
`mv Pan4709_part1data.bed Pan4709data.bed`
`mv Pan4709_part1dataSambamba.bed Pan4709dataSambamba.bed`