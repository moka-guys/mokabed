This is a VCP2 R208 test BED file for CNV analysis using ExomeDepth.
Initially Pan4712_CNV.bed was created for this but needed to updated with new genes based on the Test Directory changes.

## Save query used to extract Transcript file.
Transcript was selected from the ngspanel genes table using the query select GuysAccession, Symbol, '0' as GuysAccessionVersion from ngspanelgenes where NGSPanelID=5087 This was used to create Pan5087.txt

## Run mokabed
Time Stamp:2022-11-02 11:42:42.402397
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5087dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5087.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5087data.bed --logfile /home/dnanexus/out/Output_files/Pan5087_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add Pan3608
cat Pan3608.bed >> Pan5087data.bed

## Add Pan4350
cat Pan4350.bed >> Pan5087data.bed

## Sort and rename
sort Pan5087data.bed -k1,1V -k2,2n -k3,3n > Pan5087_sorted.bed;mv Pan5087data.bed Pan5087_unsorted.bed; mv Pan5087_sorted.bed Pan5087data.bed; rm Pan5087_unsorted.bed

## Manually remove header from Pan5087data.bed

## Convert to 4 column format
cut -f 1-4 Pan5087data.bed > Pan5087data_4col.bed; rm Pan5087data.bed; mv Pan5087data_4col.bed Pan5087data.bed

## Rename file to make it clear that it's a CNV BED
mv Pan5087data.bed Pan5087_CNV.bed

## Delete unrequired files
rm Pan5087dataSambamba.bed

## Testing
Testing performed in 003_221102_mokabed_Pan5087. Job ran without error.