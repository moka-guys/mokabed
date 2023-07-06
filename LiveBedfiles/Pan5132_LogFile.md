This BED file is a remake of Pan5119, the VCP2 +/-30bp panel, but with the 5UTR padded by +/-30bp

## Run Mokabed
Time Stamp:2023-06-27 12:46:55.477306
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5132dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5132.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5132data.bed --logfile /home/dnanexus/out/Output_files/Pan5132_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add Pan4283
cat Pan4283.bed >> Pan5132data.bed

## Remove duplicate chek2 region
Pan4283 contains a region of chek2. The whole of chek2(rs555607708) is now included so this region does not need to be specified so it was removed manually.

## Add Pan5117
cat Pan5117.bed >> Pan5132data.bed

## Add Pan3610
cat Pan3610.bed >> Pan5132data.bed

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

2. Replace Entrez IDs with gene symbols
    Open Pan5132_capture.bed in Excel, first in split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol.
    Delete Gene Accession column

    Excel saves file as a csv, so open file in VS code and replace "," with a tab
    This helps visualise changes during code review

    Delete EntrezID column

    In Excel format Entrez;Gene_Accession to only include gene symbol
        a) Remove ";" at the end of intronic regions in Entrez;Gene_Accession column (if not done, leaves empty cells in the next step)
        b) Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols.
                Find *; and and leave replace field empty (remember to select wildcard option)
                Excel saves output as csv, replace "," with a tab

        

