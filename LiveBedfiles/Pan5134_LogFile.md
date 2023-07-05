## Pan5134
This VCP1 BED file is based on Pan4398, but all genes 5UTRs were padded by 30bp.

## Run mokabed
Time Stamp:2023-06-29 13:11:16.257316
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5134dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5134.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5134data.bed --logfile /home/dnanexus/out/Output_files/Pan5134_LogFile.txt 

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
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed >> Pan5134data.bed

## Sort data.bed
sort Pan5134data.bed -k1,1V -k2,2n -k3,3n > Pan5134data_sorted.bed; mv Pan5134data.bed Pan5134data_unsorted.bed; mv Pan5134data_sorted.bed Pan5134data.bed; rm Pan5134data_unsorted.bed

move header to the top

## Fix LAMA2 exon
One of the LAMA2 exons was mapped incorrectly.
The incorrect coordinates are: chr6:129763336-129763402 and the correct coordinates - chr6:129764177-129764243

## Testing
Pan5134data.bed was test using mokapicard, job completed without error.

