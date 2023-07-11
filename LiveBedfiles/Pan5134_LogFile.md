## Pan5134
This VCP1 BED file is based on Pan4398, but all genes UTRs were padded by 30bp.

## Run mokabed
Time Stamp:2023-07-11 13:45:34.972424
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5134dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --down 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5134.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5134data.bed --logfile /home/dnanexus/out/Output_files/Pan5134_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add regions from duplicate transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5134_duplicatesdata.bed -b Pan5134data.bed >> Pan5134data.bed

# Delete any unrequired files
rm Pan5134dataRefSeqFormat.txt Pan5134_duplicatesdataSambamba.bed Pan5134_duplicatesdataRefSeqFormat.txt Pan5134dataSambamba.bed Pan5134_duplicatesdata.bed Pan5134_duplicates_LogFile.txt

## Add in the additional panels.
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed Pan3608.bed >> Pan5134data.bed