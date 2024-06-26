# Pan4814
This BED file is to be used for exome depth variant calling for R209,210 and 211 (these tests have a large number of genes in common).
In addition to the transcripts listed two additional BED files are to be included (Pan3608 and Pan4350)

## Run MokaBED

Time Stamp:2021-12-08 21:55:45.867246
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4814dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4814.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4814data.bed --logfile /home/dnanexus/out/Output_files/Pan4814_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## concatenate additional BED files
`cat Pan3608.bed >> Pan4814data.bed`
`cat Pan4350.bed >> Pan4814data.bed`

## sort bedfile
`sort Pan4814data.bed -k1,1V -k2,2n -k3,3n > Pan4814_sorted.bed;mv Pan4814data.bed Pan4814_unsorted.bed; mv Pan4814_sorted.bed Pan4814data.bed; rm Pan4814_unsorted.bed`

## Manually remove header from Pan4814data.bed

## Convert to 4 column format
`cut -f 1-4 Pan4814data.bed > Pan4814data_4col.bed; rm Pan4814data.bed; mv Pan4814data_4col.bed Pan4814data.bed`

## Rename file to make it clear that it's a CNV BED 
`git mv Pan4814data.bed Pan4814_CNV.bed`

## remove unrequired files
`rm Pan4814dataSambamba`