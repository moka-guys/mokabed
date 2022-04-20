# Pan4949

This BEDfile is a rename of Pan4301, the VCP2 +/-10bp panel, but this time with the whole of CHEK2 gene.

This panel consists of a number of genes which are to be padded +/-10 and one gene, PTEN which also requires the 5' UTR (also padded 10bp).
## Run MokaBED (This covers all genes except for PTEN - see Pan4949_PTEN_logfile.txt)
Time Stamp:2022-04-20 12:16:26.211789
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4949dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 10 --down 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4949.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4949data.bed --logfile /home/dnanexus/out/Output_files/Pan4949_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add PTEN to data.bed
`cat Pan4949_PTENdata.bed >> Pan4949data.bed`
(header and sorting to follow)

## Add Pan4283
`cat Pan4283.bed >> Pan4949data.bed`

## remove duplicate chek2 region and extra header
Pan4283 contains a region of chek2. The whole of chek2 is now included so this region does not need to be specified so it was removed manually

extra header removed

## sort Pan4949data.bed
`sort Pan4949data.bed -k1,1V -k2,2n -k3,3n > Pan4949data_sorted.bed; mv Pan4949data.bed Pan4949data_unsorted.bed; mv Pan4949data_sorted.bed Pan4949data.bed; rm Pan4949data_unsorted.bed`
move header to the top manually

## make Pan4949_flat.bed
`cut -f1-3 Pan4949data.bed | bedtools merge > Pan4949_flat.bed`
Flat bed file used for somatic variant calling.