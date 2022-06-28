## Pan4992
This BED file will be used to filter CNV variant calls for R122. It contains 2 genes which is to be padded +/-30bp and include the 5' UTR, also padded by 30bp.
The VCP_CNV_control_sites (Pan3608) will also be added.
The CNV bedfile is a 4 column bedfile, named Panxxx_CNV.bed

### Run Mokabed
Time Stamp:2022-06-28 07:44:11.709187
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4992dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4992.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4992data.bed --logfile /home/dnanexus/out/Output_files/Pan4992_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

### Add Pan3608
`cat Pan3608.bed >> Pan4992data.bed`

### Sort data.bed
`sort Pan4992data.bed -k1,1V -k2,2n -k3,3n > Pan4992_sorted.bed;mv Pan4992data.bed Pan4992_unsorted.bed; mv Pan4992_sorted.bed Pan4992data.bed; rm Pan4992_unsorted.bed`

### remove header manually

### Convert to 4 column format
`cut -f 1-4 Pan4992data.bed > Pan4992data_4col.bed; rm Pan4992data.bed; mv Pan4992data_4col.bed Pan4992data.bed`

### rename to _cnv.bed
`git mv Pan4992data.bed Pan4992_CNV.bed`

### delete unrequired files
`git rm Pan4992dataSambamba.bed Pan4992dataRefSeqFormat.txt`

### testing
The bedfile was tested with ED_cnv_calling_v1.0.0 in 003_220628_Pan4991-4994 and the job ran without error