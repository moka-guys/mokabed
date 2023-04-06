This BED file is a remake of Pan4948, the VCP2 +/-10bp panel, but with the following changes:
- whole of SCG5 gene,
- 6 genomic targets that lie between SCG5 and GREM1 (Pan5117)
- extra UTR regions (Pan5120)
- updated trancript of POLD1 gene to NM_002691

## Save transcripts
PTEN gene included separetly as it also requires the 5' UTR (also padded 10bp).

## Run mokabed- This covers all genes except for PTEN - see Pan5123_PTEN_LogFile.txt
Time Stamp:2023-04-06 14:37:51.008320
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5123dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5123.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5123data.bed --logfile /home/dnanexus/out/Output_files/Pan5123_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add PTEN
cat Pan5123_PTENdata.bed >> Pan5123data.bed

remove header manually

## Add Pan4283
cat Pan4283.bed >> Pan5123data.bed

## Remove duplicate chek2 region
Pan4283 contains a region of chek2. The whole of chek2 is now included so this region does not need to be specified so it was removed manually.

## Add Pan5117
cat Pan5117.bed >> Pan5123data.bed

## Add Pan5120
cat Pan5120.bed >> Pan5123data.bed

## Sort Pan5123data.bed
sort Pan5123data.bed -k1,1V -k2,2n -k3,3n > Pan5123data_sorted.bed; mv Pan5123data.bed Pan5123data_unsorted.bed; mv Pan5123data_sorted.bed Pan5123data.bed; rm Pan5123data_unsorted.bed move header to the top manually

## Make Pan5123_flat.bed
cut -f1-3 Pan5123data.bed | bedtools merge > Pan5123_flat.bed Flat bed file used for somatic variant calling.