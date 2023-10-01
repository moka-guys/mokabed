# Pan5168
This bedfile will be used to perform the variant filtering step of exome depth for R79. It contains genes for this test (as of Summer 2023) padded by +/-30 bp. Pan3608 (control sites) has also been included.

# Run Mokabed
Time Stamp:2023-09-29 16:40:57.414260
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5168dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5168.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5168data.bed --logfile /home/dnanexus/out/Output_files/Pan5168_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add in the additional panels.
cat Pan5168data.bed Pan3608.bed  >> Pan5168data.bed

## Sort data.bed
sort Pan5168data.bed -k1,1V -k2,2n -k3,3n > Pan5168_sorted.bed;mv Pan5168data.bed Pan5168_unsorted.bed; mv Pan5168_sorted.bed Pan5168data.bed; rm Pan5168_unsorted.bed

Remove header

# Convert to 4 column format
cut -f 1-4 Pan5168data.bed > Pan5168data_4col.bed; rm Pan5168data.bed; mv Pan5168data_4col.bed Pan5168data.bed

# Rename to _cnv.bed
git mv Pan5168data.bed Pan5168_CNV.bed

