# Pan5206
This bedfile will be used to perform the variant filtering step of exome depth for R210. It contains genes for this test (as of Summer 2023) 5' UTRs are also included but no regions are padded. Two BEDfiles containing additional regions are also inlcuded - Pan3608 (control sites) and Pan4765 (intronic regions specific to R210 genes).

# Run Mokabed
Time Stamp:2023-12-18 14:20:44.620843
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5206dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5206.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5206data.bed --logfile /home/dnanexus/out/Output_files/Pan5206_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add in the additional panels.
cat Pan4765.bed Pan3608.bed >> Pan5206data.bed

# Sort data.bed
sort Pan5206data.bed -k1,1V -k2,2n -k3,3n > Pan5206_sorted.bed;mv Pan5206data.bed Pan5206_unsorted.bed; mv Pan5206_sorted.bed Pan5206data.bed; rm Pan5206_unsorted.bed

# Remove header
This was done manually

# Convert to 4 column format
cut -f 1-4 Pan5206data.bed > Pan5206data_4col.bed; rm Pan5206data.bed; mv Pan5206data_4col.bed Pan5206data.bed