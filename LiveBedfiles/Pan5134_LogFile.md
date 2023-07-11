## Pan5134
This VCP1 BED file is based on Pan4398, but all genes UTRs were padded by 30bp.

## Run mokabed
Time Stamp:2023-07-11 13:45:34.972424
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5134dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --down 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5134.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5134data.bed --logfile /home/dnanexus/out/Output_files/Pan5134_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add regions from duplicate transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5134_duplicatesdata.bed -b Pan5134data.bed >> Pan5134data.bed

# Delete any unrequired files
rm Pan5134dataRefSeqFormat.txt Pan5134_duplicatesdataSambamba.bed Pan5134_duplicatesdataRefSeqFormat.txt Pan5134dataSambamba.bed Pan5134_duplicatesdata.bed Pan5134_duplicates_LogFile.txt

## Add in the additional panels.
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed Pan3608.bed >> Pan5134data.bed

## Sort data.bed
sort Pan5134data.bed -k1,1V -k2,2n -k3,3n > Pan5134data_sorted.bed; mv Pan5134data.bed Pan5134data_unsorted.bed; mv Pan5134data_sorted.bed Pan5134data.bed; rm Pan5134data_unsorted.bed

move header to the top

## Fix LAMA2 exon
One of the LAMA2 exons was mapped incorrectly.
The incorrect coordinates are: chr6:129763336-129763402 and the correct coordinates - chr6:129764177-129764243

## Testing
Pan5134data.bed was test using mokapicard, job completed without error.

## Creating Exomedepth readcount BED file

1. Create a copy of Pan5134data.bed to make changes
    cp Pan5134data.bed Pan5134_capture.bed

2. Replace Entrez IDs with gene symbols
    Open Pan5134_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating 
    EntrezID;GeneSymbol.
    Excel saves file as a csv, so open file in VS code and replace "," with a tab
    This helps visualise changes during code review

    In Excel format Entrez;Gene_Accession to only include gene symbol
    a) Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols.
                Find *; and and leave replace field empty (remember to select wildcard option)
                Excel saves output as csv, in VScode replace "," with a tab

    b) Step above left additionally added regions with empty cells in Gene_Accession column. Manually copy EntrezID field into      Gene_accession column.

    c) Delete Entrez ID column

3. Convert 4 column format
    Excel saves output as csv, in VScode replace "," with a tab
    cut -f1-4 Pan5134_capture.bed > Pan5134data_4col.bed

4. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

5. Generate intermediary exomedepth files for exons
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5134 Pan5134data_4col.bed