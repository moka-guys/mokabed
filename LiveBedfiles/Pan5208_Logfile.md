## Pan5208
This VCP1 Exomedepth readcount BED file it is a remake of Pan5191. LDLR and PCSK9 were accidentally excluded from the bed file. Pan5206 will have up and down coding regions included and the 5UTR - no regions have been padded.

Additional regions were included in this BED file: 
Pan4291.bed- intronic variants relevant to Haematological genes 
Pan4290.bed- intronic variants for VCP1 regions 
Pan4292.bed- FH intronic variants padded by 5bp Pan4272.bed- intronic variants for CF 
Pan3608.bed- additional CNV regions

# Save transcript files

# Run mokabed
Time Stamp:2024-02-23 11:52:18.863593
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5208dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5208.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5208data.bed --logfile /home/dnanexus/out/Output_files/Pan5208_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add regions from extra transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5208_extradata.bed -b Pan5208data.bed >> Pan5208data.bed

# Add additional panels
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed Pan3608.bed >> Pan5208data.bed

# Sort data.bed
sort Pan5208data.bed -k1,1V -k2,2n -k3,3n > Pan5208data_sorted.bed; mv Pan5208data.bed Pan5208data_unsorted.bed; mv Pan5208data_sorted.bed Pan5208data.bed; rm Pan5208data_unsorted.bed

Move header to the top

# Fix LAMA2 exon (without padding)
One of the LAMA2 exons was mapped incorrectly. The incorrect coordinates are: chr6:129763366-129763372 and the correct coordinates - chr6:129764207-129764213

# Check all requested genes present 

a) Take a copy of Pan5208data.bed to convert into a 6 column bed file.
    cp Pan5208data.bed Pan5208data_6col.csv

b) Open Pan5208data_6col.csv in Excel, separating the GeneAccession column on “;” and delete empty columns between EntrezID column  and GeneAccession column

c) Delete first row, contains date e.g #2023-10-10 10:41:52.716212

d) Rename header to: Chr, Start, Stop, EntrezID, Gene, Transcript