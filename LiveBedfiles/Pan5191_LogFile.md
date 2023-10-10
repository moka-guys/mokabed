## Pan5191
This VCP1 BED file is based on Pan4398, 5UTR was included- no regions have been padded.

# Run Mokabed
Time Stamp:2023-10-10 10:41:41.354574
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5191dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5191.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5191data.bed --logfile /home/dnanexus/out/Output_files/Pan5191_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add regions from duplicate transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5191_duplicatesdata.bed -b Pan5191data.bed >> Pan5191data.bed

# Delete any unrequired files
rm Pan5191dataRefSeqFormat.txt Pan5191_duplicatesdataSambamba.bed Pan5191_duplicatesdataRefSeqFormat.txt Pan5191dataSambamba.bed Pan5191_duplicatesdata.bed Pan5191_duplicates_LogFile.txt