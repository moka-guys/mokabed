## Pan5179

This bedfile will be used to perform the variant filtering step of exome depth for R229. It contains genes for this test (as of Summer 2023) padded by +/-30 bp. Pan3608 (control sites) and Pan5167 (intronic sites) have also been included.

# Run mokabed
Time Stamp:2023-10-03 17:23:51.684259
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5179dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5179.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5179data.bed --logfile /home/dnanexus/out/Output_files/Pan5179_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add in the additional panels.
cat Pan3608.bed >> Pan5179data.bed

cat Pan5167.bed >> Pan5179data.bed

# Sort data.bed
sort Pan5179data.bed -k1,1V -k2,2n -k3,3n > Pan5179_sorted.bed;mv Pan5179data.bed Pan5179_unsorted.bed; mv Pan5179_sorted.bed Pan5179data.bed; rm Pan5179_unsorted.bed

remove header

# Convert to 4 column format
cut -f 1-4 Pan5179data.bed > Pan5179data_4col.bed; rm Pan5179data.bed; mv Pan5179data_4col.bed Pan5179data.bed

# Rename to _cnv.bed
git mv Pan5179data.bed Pan5179_CNV.bed

# Delete unrequired files
git rm Pan5179dataSambamba.bed Pan5179dataRefSeqFormat.txt

# Testing
The bedfile was tested with ED_cnv_calling_v1.2.0 in 230822_VCP3_exomedepth_bedfiles and the job ran without error