# Pan5217

This is a remake of the VCP3 exomedepth readcount BEDfile.

During the validation of Pan5211_exomedepth.bed(https://github.com/moka-guys/mokabed/blob/master/LiveBedfiles/Pan5211_exomedepth.bed) it was noticed CARS1 gene was missing.

The process of generating a VCP3 Exomedepth readcount bedfile is very complicated, the quickest solution to this problem without restarting from scratch, was to create the CARS1 bedfile seperately and join the output with Pan5211 creating Pan5217_exomedepth.bed

## Save CARS1 transcript file

## Run Mokabed for CARS1
Time Stamp:2024-03-15 09:49:19.826707
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/cars_transcriptdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/cars_transcript.txt --minuschr --outputfile /home/dnanexus/out/Output_files/cars_transcriptdata.bed --logfile /home/dnanexus/out/Output_files/cars_transcript_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

#############
Create CARS1 exomedepth bedile
#############

## Replace Entrez ID with gene symbols

a) Open cars_transcriptdata.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab. This helps visualise changes during code review

b) In Excel format Entrez;Gene_Accession to only include gene symbol. Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

c) Delete Entrez ID column

## Convert 4 column format
cut -f1-4 cars_transcriptdata.bed > cars_transcriptdata_4col.bed

## Run makeExomedepth.sh
Generate intermediary exomedepth files for exons:
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _CARS1 cars_transcriptdata_4col.bed

## Rename exomedepth file
git mv _CARS1_exomedepth.bed CARS1_exomedepth.bed

## Delete unrequired files
rm _CARS*