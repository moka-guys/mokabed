# Pan5152
This bedfile will be used to perform the variant filtering step of exome depth for R207. It contains genes for this test (as of Summer 2023) padded by +/-30 bp. 5' UTRs are also included, and padded +/-30bp. Two BEDfiles containing additional regions are also inlcuded - Pan3608 (control sites) and Pan5151 (intronic regions specific to R207 genes)

## run mokabed
Time Stamp:2023-07-25 15:44:01.867840
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5152dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5152.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5152data.bed --logfile /home/dnanexus/out/Output_files/Pan5152_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add in the additional panels.
`cat Pan5151.bed Pan3608.bed  >> Pan5152data.bed`

## Sort data.bed
`sort Pan5152data.bed -k1,1V -k2,2n -k3,3n > Pan5152_sorted.bed;mv Pan5152data.bed Pan5152_unsorted.bed; mv Pan5152_sorted.bed Pan5152data.bed; rm Pan5152_unsorted.bed`

# Remove header 
This was done manually

# Convert to 4 column format
`cut -f 1-4 Pan5152data.bed > Pan5152data_4col.bed; rm Pan5152data.bed; mv Pan5152data_4col.bed Pan5152data.bed`

# Rename to _cnv.bed
`git mv Pan5152data.bed Pan5152_CNV.bed`

# Delete unrequired files
`git rm Pan5152dataSambamba.bed Pan5152dataRefSeqFormat.txt`