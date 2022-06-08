# Pan4969 logfile
This BED file is used to calculate coverage for the TSO500 panel.
It consists of a subset of the 500+ genes on the panel, which are used for clinical reporting.
As per the bed file request form there are multiple transcripts per gene and a seperate BED file containing intronic regions to be added.
This new version of the TSO500 coverage bedfile contains additional genes and therefore will replace the previous bed file (Pan4963).

## Transcript files
There are multiple transcripts for several of the genes request. Four transcript files were created manually to ensure no duplicate transcripts were included. These are saved as Pan4969_transcripts1-4.txt/
Files reformated with amended headers to match format required by mokabed. Accession added as 0 as will not be used by script anyway.
Transcripts2 and transcripts4 files were still in incorrect format- updated.

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
