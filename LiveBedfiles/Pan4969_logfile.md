# Pan4969 logfile
This BED file is used to calculate coverage for the TSO500 panel.
It consists of a subset of the 500+ genes on the panel, which are used for clinical reporting.
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.
This new version of the TSO500 coverage bedfile contains additional genes and therefore will replace the previous bed file (Pan4963).

## Transcript files
There are multiple transcripts for several of the genes request. Four transcript files were created manually to ensure no duplicate transcripts were included. These are saved as Pan4969_transcripts1-4.txt/
Files reformated with amended headers to match format required by mokabed. Accession added as 0 as will not be used by script anyway.
Transcripts2 and transcripts4 files were still in incorrect format- updated.

The transcript files were checked by comparing the number of transcripts in the request form with the total number across the 4 transcript files (122). The files were also visually inspected to check for duplicates and errors. 

## Run mokabed
mokabed run in DNAnexus 003_220608_Pan4969
Example command: 
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=project-GBQFFGQ0xzbv5Q1b4Q3Gx38k:file-GBQGq600xzbQ5k2V7bXPQzBP -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

All 4 sets of transcripts were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below.
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4969_transcripts1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4969_transcripts1data.bed --logfile /home/dnanexus/out/Output_files/Pan4969_transcripts1_LogFile.txt`

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4969_transcripts2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4969_transcripts2data.bed --logfile /home/dnanexus/out/Output_files/Pan4969_transcripts2_LogFile.txt`

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4969_transcripts3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4969_transcripts3data.bed --logfile /home/dnanexus/out/Output_files/Pan4969_transcripts3_LogFile.txt`

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4969_transcripts4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4969_transcripts4data.bed --logfile /home/dnanexus/out/Output_files/Pan4969_transcripts4_LogFile.txt`

## combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

### parts 3 and 4
`bedtools subtract -a 'Pan4969_transcripts4data.bed' -b 'Pan4969_transcripts3data.bed' >> Pan4969_transcripts3data.bed`
This resulted in no additonal regions being added.

Part 4 BED files were deleted
`rm Pan4969_transcripts4data*`

### parts 2 and 3
    

Remove part 3 bed files
`rm Pan4969_transcripts3data*`

### parts 1 and 2
`bedtools subtract -a 'Pan4969_transcripts2data.bed' -b 'Pan4969_transcripts1data.bed' >> Pan4969_transcripts1data.bed`
`bedtools subtract -a 'Pan4969_transcripts2dataSambamba.bed' -b 'Pan4969_transcripts1dataSambamba.bed' >> Pan4969_transcripts1dataSambamba.bed`

Remove part 2 bed files
`rm Pan4969_transcripts2data*`

## Add intronic regions
concatenate intronic regions (Pan4968) into data.bed
`cat Pan4968.bed >> Pan4969_transcripts1data.bed`

manually modify the intronic regions to match data.bed format (EntrezID taken from other MET regions, or from Pan4963 for TERT)

concatenate intronic regions (Pan4968) into dataSambamba.bed
`cat Pan4968.bed >> Pan4969_transcripts1dataSambamba.bed`

intronic regions edited manually to match sambamba format in Pan4963_part1dataSambamba.bed 

files not saved after manual modification. Saved now.

## sort bedfiles
### data.bed
`mv Pan4969_transcripts1data.bed Pan4969_transcripts1data_unsorted.bed; sort Pan4969_transcripts1data_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4969_transcripts1data.bed; rm Pan4969_transcripts1data_unsorted.bed`
header moved to top manually

### dataSambamba.bed
`mv Pan4969_transcripts1dataSambamba.bed Pan4969_transcripts1dataSambamba_unsorted.bed; sort Pan4969_transcripts1dataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4969_transcripts1dataSambamba.bed; rm Pan4969_transcripts1dataSambamba_unsorted.bed`

## add chr
Added chr manually- shown to be required in previous testing for Pan4709

## rename
`mv Pan4969_transcripts1data.bed Pan4969data.bed`
`mv Pan4969_transcripts1dataSambamba.bed Pan4969dataSambamba.bed`

## testing
These bed files were tested using sambamba coverage and moka picard apps.
The sambamba app was run on the HD200 sample from TSO23006 using the original dx run command, modified to use the correct BED file and output to the Pan5110 test project. App completed without error.

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-G6vyyf00jy1kPkX9PJ1YkxB1 --detach -y --brief --name=TSO23006_01_220246_HD200_Pan5085.bam -ibam_index=file-GPZJF380f81Z1zK8yy6F5p6k -ibamfile=file-GPZJF380f81XJq0f6xP19xJP -icoverage_level=100 -isambamba_bed=003_230126_Pan5110:/Pan5110dataSambamba.bed -imerge_overlapping_mate_reads=true -iexclude_failed_quality_control=true -iexclude_duplicate_reads=true -imin_base_qual=25 -imin_mapping_qual=30 --dest=003_230126_Pan5110`

The MokaPicard app was previously found to fail with TSO500 bam files, presumed to be due to an issue with the bam. Therefor this bed file was tested with the NA12878 bam file from NGS482B (VCP3). App completed successfully suggesting the bed file is valid.

## delete extra files
`rm Pan4969_transcripts1dataRefSeqFormat.txt`
