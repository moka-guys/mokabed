# Pan5223
This bedfile will be used to perform the variant filtering step of exome depth for R90. It is a remake of Pan5223; it is a known issue that mokabed mapps exon 18 of DIAPH1 incorrectly. While this issue was manually rectified in the VCP3 readcount bedfile (Pan5217), it was not corrected in Pan5171.

Additionally, TBXA2R will be updated to use the MANE transcript NM_001060.

## Save transcript file and request form

## Run mokabed
Time Stamp:2024-04-03 11:57:57.594913
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5223dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5223.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5223data.bed --logfile /home/dnanexus/out/Output_files/Pan5223_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add additional panels
cat Pan3608.bed >> Pan5223data.bed

## Sort data.bed
sort Pan5223data.bed -k1,1V -k2,2n -k3,3n > Pan5223_sorted.bed;mv Pan5223data.bed Pan5223_unsorted.bed; mv Pan5223_sorted.bed Pan5223data.bed; rm Pan5223_unsorted.bed

remove header

## Fix DIAPH1 (no padding)
incorrect 5:140915620-140915629

corrected to  5:140950994-140951003


