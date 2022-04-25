# Pan4948

This BEDfile is a rename of Pan4310, the VCP2 +/-30bp panel, but this time with the whole of CHEK2 gene.

This panel consists of a number of genes which are to be padded +/-30 and one gene, PTEN which also requires the 5' UTR (also padded 30bp).
## Run MokaBED (This covers all genes except for PTEN - see Pan4948_PTEN_logfile.txt)
Time Stamp:2022-04-22 16:29:13.085148
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4948dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4948.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4948data.bed --logfile /home/dnanexus/out/Output_files/Pan4948_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add PTEN
`cat Pan4948_PTENdata.bed >> Pan4948data.bed`
(header and sorting to follow)
remove header manually