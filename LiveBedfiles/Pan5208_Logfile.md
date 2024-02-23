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