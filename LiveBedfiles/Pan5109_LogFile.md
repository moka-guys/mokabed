This is RPKM BED file for VCP2 padded by 50bp 

# Save the transcript file

# Run mokabed
Time Stamp:2023-04-12 14:48:18.034598
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5109dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --up 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5109.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5109data.bed --logfile /home/dnanexus/out/Output_files/Pan5109_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# run nexus app to create RPKM Bedfile
performed in 003_230303_R211_mokabed
see Pan5109_RPKM_logfile.txt

# testing statement
Pan5109_RPKM.bed was tested using RPKM_using_conifer_v1.6. The app finished successfully.

# sorting the BED file to ease analysis
sort Pan5109_RPKM.bed -k1,1V -k2,2n -k3,3n > Pan5109_RPKM_sorted.bed; mv Pan5109_RPKM.bed Pan5109_RPKM_unsorted.bed; mv Pan5109_RPKM_sorted.bed Pan5109_RPKM.bed; rm Pan5109_RPKM_unsorted.bed

# testing

Pan5109_RPKM.bed tested again after sorting using RPKM_using_conifer_v1.6 and the app finished successfully.