## Pan4994
This BED file will be used to filter CNV variant calls for R124. It contains 2 genes which is to be padded +/-30bp and include the 5' UTR, also padded by 30bp.
The VCP_CNV_control_sites (Pan3608) will also be added.
The CNV bedfile is a 4 column bedfile, named Panxxx_CNV.bed

### run mokabed
Time Stamp:2022-06-28 07:45:39.617205
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4994dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4994.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4994data.bed --logfile /home/dnanexus/out/Output_files/Pan4994_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2