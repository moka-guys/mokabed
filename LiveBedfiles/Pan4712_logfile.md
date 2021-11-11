This is a VCP2 R208 test BED file for CNV analysis using ExomeDepth.

## Save query used to extract Transcript file.
Transcript was selected from the ngspanel genes table using the query
`select GuysAccession, Symbol, '0' as GuysAccessionVersion from ngspanelgenes where NGSPanelID=4712`
This was used to create Pan4712.txt

## Run mokabed
Time Stamp:2021-11-11 12:30:33.533732
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4712dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4712.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4712data.bed --logfile /home/dnanexus/out/Output_files/Pan4712_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add Pan3608
cat Pan3608.bed >> Pan4712data.bed

## Add Pan4350
cat Pan4350.bed >> Pan4712data.bed
