# Pan5171
This bedfile will be used to perform the variant filtering step of exome depth for R90. It contains genes for this test (as of Summer 2023) padded by +/-30 bp. Pan3608 (control sites) has also been included.

# Run mokabed
Time Stamp:2023-10-01 22:59:42.888604
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5171dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5171.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5171data.bed --logfile /home/dnanexus/out/Output_files/Pan5171_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add in the additional panels.
cat Pan5171data.bed Pan3608.bed  >> Pan5171data.bed

## Sort data.bed
sort Pan5171data.bed -k1,1V -k2,2n -k3,3n > Pan5171_sorted.bed;mv Pan5171data.bed Pan5171_unsorted.bed; mv Pan5171_sorted.bed Pan5171data.bed; rm Pan5171_unsorted.bed

remove header
