Time Stamp:2021-01-11 16:37:30.580568
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4118dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4118.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4118data.bed --logfile /home/dnanexus/out/Output_files/Pan4118_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Pan4118
This BED file contains the same regions as Pan4003 but padded to +/-30bp.
2 genes have multiple transcripts. These were split into seperate files.
MokaBED was run for both transcript lists (see above logs and Pan4118_duplicates_logfile.txt)

### Add regions from duplicate transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file. 
bedtools subtract -a Pan4118_duplicatesdata.bed -b Pan4118data.bed >> Pan4118data.bed

### sort and rename to make review easier
sort Pan4118data.bed -k1,1V -k2,2n -k3,3n > Pan4118data_sorted.bed; mv Pan4118data.bed Pan4118data_unsorted.bed; mv Pan4118data_sorted.bed Pan4118data.bed

move header back to top manually

### Add regions from duplicate transcripts to sambamba.bed
bedtools subtract -a Pan4118_duplicatesdataSambamba.bed -b Pan4118dataSambamba.bed  >> Pan4118dataSambamba.bed

### sort and rename to make review easier
sort Pan4118dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4118dataSambamba_sorted.bed; mv Pan4118dataSambamba.bed Pan4118dataSambamba_unsorted.bed; mv Pan4118dataSambamba_sorted.bed Pan4118dataSambamba.bed; rm Pan4118dataSambamba_unsorted.bed

### Delete intermediate and RefSeq files (since it is no longer accurate and not used)
rm Pan4118dataRefSeqFormat.txt Pan4118_duplicatesdata.bed Pan4118_duplicatesdataRefSeqFormat.txt Pan4118_duplicatesdataSambamba.bed
