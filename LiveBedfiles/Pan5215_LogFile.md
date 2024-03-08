# Pan5215
This is a VCP1 R134 test BED file for CNV analysis using ExomeDepth. No padding was been added to the exons and 5UTR has been included.

**NOTE**: 5UTRS were requested to be padded by 30bp to capture CNVs extending beyond the 5UTR. However, Exomedepth reports full length of any CNV overlapping with any region given in the bedfile, therefore there is no value padding the 5UTR.

# Run mokabed
Time Stamp:2024-03-07 15:44:03.090129
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5215dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5215.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5215data.bed --logfile /home/dnanexus/out/Output_files/Pan5215_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add Pan3608

cat Pan3608.bed >> Pan5215data.bed

# Sort and rename 
sort Pan5215data.bed -k1,1V -k2,2n -k3,3n > Pan5215_sorted.bed;mv Pan5215data.bed Pan5215_unsorted.bed; mv Pan5215_sorted.bed Pan5215data.bed; rm Pan5215_unsorted.bed

# Manually remove header from Pan5215data.bed

# Convert to 4 column format
cut -f 1-4 Pan5215data.bed > Pan5215data_4col.bed; rm Pan5215data.bed; mv Pan5215data_4col.bed Pan5215data.bed

# Rename file to make it clear that it's a CNV BED 
mv Pan5215data.bed Pan5215_CNV.bed

# delete unrequired files
rm Pan5215dataSambamba.bed

# Testing
testing performed in 003_240223_exomedepth_bedfiles. Job ran without error.