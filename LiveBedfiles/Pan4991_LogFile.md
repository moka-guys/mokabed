## Pan4991
This BED file will be used to filter CNV variant calls for R120. It contains 1 gene which is to be padded +/-30bp and include the 5' UTR, also padded by 30bp.
The VCP_CNV_control_sites (Pan3608) will also be added.
The CNV bedfile is a 4 column bedfile, named Panxxx_CNV.bed

### Run Mokabed
Time Stamp:2022-06-28 07:43:25.909489
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4991dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4991.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4991data.bed --logfile /home/dnanexus/out/Output_files/Pan4991_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

### Add Pan3608
`cat Pan3608.bed >> Pan4991data.bed`

### Sort data.bed
`sort Pan4991data.bed -k1,1V -k2,2n -k3,3n > Pan4991_sorted.bed;mv Pan4991data.bed Pan4991_unsorted.bed; mv Pan4991_sorted.bed Pan4991data.bed; rm Pan4991_unsorted.bed`

### remove header manually

### Convert to 4 column format and rename (using git to preserve tracking (hopefully))
`cut -f 1-4 Pan4991data.bed > Pan4991data_4col.bed; rm Pan4991data.bed; mv Pan4991data_4col.bed Pan4991data.bed; git mv Pan4991data.bed Pan4991_CNV.bed`

### delete unrequired files
`git rm Pan4991dataSambamba.bed Pan4991dataRefSeqFormat.txt`

### testing
The bedfile was tested with ED_cnv_calling_v1.0.0 in 003_220628_Pan4991-4994 and the job ran without error