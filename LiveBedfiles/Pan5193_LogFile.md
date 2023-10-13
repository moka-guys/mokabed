## Pan5193
This bedfile will be used to perform the variant filtering step of exome depth for R211. It contains genes for this test (as of Summer 2023) 5' UTRs are also included but no regions are padded. Two BEDfiles containing additional regions are also inlcuded - Pan3608 (control sites), SCG5-GREM1 intronic sites (Pan5117) and Pan5154 (intronic regions specific to R211 genes).

NOTE: this is a remake of Pan5160 as it was noticed GREM1 gene was missing from the BED file. 

# Run mokabed
Time Stamp:2023-10-13 12:10:44.163297
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5193dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5193.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5193data.bed --logfile /home/dnanexus/out/Output_files/Pan5193_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2