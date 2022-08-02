## Pan5018
This BED file will be used to calculate coverage for the 4 genes currently targetted by the LRPCR assay (as per Pan4967)

As described in Pan4971 this transcript of SMN1 cuases issues with MokeBED so in this case the SMN1 gene will be added by concatenating the existing Pan4971 BED files.

### run mokabed for PMS2, CHEK2 and IKBKG
with no UTRs and 10bp paddings

Time Stamp:2022-08-02 14:16:12.507374
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5018dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5018.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5018data.bed --logfile /home/dnanexus/out/Output_files/Pan5018_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2


## add Pan4971 to data.bed
`cat Pan4971data.bed >> Pan5018data.bed`
## sort data.bed
`sort Pan5018data.bed -k1,1V -k2,2n -k3,3n > Pan5018datasorted.bed; mv Pan5018data.bed Pan5018dataunsorted.bed;  mv Pan5018datasorted.bed Pan5018data.bed; rm Pan5018dataunsorted.bed`