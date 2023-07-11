This BED file is a remake of Pan5119, the VCP2 +/-30bp panel, but with the UTRs padded by +/-30bp

## Run mokabed
Time Stamp:2023-07-11 10:37:07.733824
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5132dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --down 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5132.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5132data.bed --logfile /home/dnanexus/out/Output_files/Pan5132_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add additional regions
NOTE: Pan4283 no longer added as entire CHEK2 gene now included and BRAC1 UTRs padded by 30bp, therefore all regions in Pan4283 are covered.

# Add Pan5117
cat Pan5117.bed >> Pan5132data.bed

# Add Pan3610
cat Pan3610.bed >> Pan5132data.bed

# Add Pan3608
cat Pan3608.bed >> Pan5132data.bed

## Sort Pan5132data.bed
sort Pan5132data.bed -k1,1V -k2,2n -k3,3n > Pan5132data_sorted.bed; mv Pan5132data.bed Pan5132data_unsorted.bed; mv Pan5132data_sorted.bed Pan5132data.bed; rm Pan5132data_unsorted.bed

move header to the top manually

## delete intermediate/incomplete files
rm Pan5132dataRefSeqFormat.txt Pan5132dataSambamba.bed

## Testing
Pan5132data.bed was tested using moka_picard_v1.2.1 - job completed sucessfully

## Creating Exomedepth BED file
This BED file is used to do read count step of exome depth for CNV analysis of VCP2.

1. Create a copy of Pan5132data.bed to make changes
    cp Pan5132data.bed Pan5132_capture.bed