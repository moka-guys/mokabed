## Pan5188
This VCP2 BED file is based on Pan5119, 5UTR was included- no regions have been padded.

# Run mokabed
Time Stamp:2023-10-10 10:51:37.957122
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5188dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5188.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5188data.bed --logfile /home/dnanexus/out/Output_files/Pan5188_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add additional regions
NOTE: Pan4283 no longer added as entire CHEK2 gene now included and BRAC1 UTRs are included, therefore all regions in Pan4283 are covered.

cat Pan5117.bed Pan3610.bed Pan3608.bed >> Pan5188data.bed

## Sort Pan5188data.bed
sort Pan5188data.bed -k1,1V -k2,2n -k3,3n > Pan5188data_sorted.bed; mv Pan5188data.bed Pan5188data_unsorted.bed; mv Pan5188data_sorted.bed Pan5188data.bed; rm Pan5188data_unsorted.bed

move header to the top manually

## delete intermediate/incomplete files
rm Pan5188dataRefSeqFormat.txt Pan5188dataSambamba.bed