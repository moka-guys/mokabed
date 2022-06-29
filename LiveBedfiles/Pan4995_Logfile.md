# Pan4995
This BED file describes the regions to be assessed (QC, coverage and variant filtering) for SNV variant calling on the VCP3 capture panel which has been updated In June 2022 to meet the changing test directory.

This BED file will be a modification to the existing VCP3 BED file, Pan4535. Pan4535 is the result of a few iterations and improvements from Pan4278 -> Pan4361 (corrected mapping of small exons in LAMA1,DIAPH1 and NBEA) and Pan4361 -> Pan4535 (addition of SNORD118 RNA).

This update includes a number of extra genes which have been added (see Pan4995_extras.txt) and a subset of genes that are already on the panel, but have some extra capture baits added to target promotor regions. These will be added with 5' UTRs padded by 10bp and only regions not already in Pan4535 will be incorporated (see Pan4995_extras_UTRs.txt)

## run mokabed for Pan4995_extras and Pan4995_extras_UTRs
`cat Pan4995_extras_LogFile.txt >> Pan4995_Logfile.md`
`cat Pan4995_extras_UTRs_LogFile.txt >> Pan4995_Logfile.md`

### Pan4995_extras mokabed
Time Stamp:2022-06-28 16:40:41.435955
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4995_extrasdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4995_extras.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4995_extrasdata.bed --logfile /home/dnanexus/out/Output_files/Pan4995_extras_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

### Pan4995_extras_UTRs mokabed
Time Stamp:2022-06-28 16:40:42.896945
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4995_extras_UTRsdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4995_extras_UTRs.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4995_extras_UTRsdata.bed --logfile /home/dnanexus/out/Output_files/Pan4995_extras_UTRs_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2
