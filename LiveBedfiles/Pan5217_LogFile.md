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

## copy Pan5211_exomedepth.bed

cp Pan5211_exomedepth.bed Pan5217_exomedepth.bed

## combine CARS1_exomedepth.bed

cat CARS1_exomedepth.bed >> Pan5217_exomedepth.bed

## Sort and rename
sort Pan5217_exomedepth.bed -k1,1V -k2,2n -k3,3n > Pan5217_exomedepth_sorted.bed; mv Pan5217_exomedepth.bed Pan5217_exomedepth.bed_unsorted.bed; mv Pan5217_exomedepth_sorted.bed Pan5217_exomedepth.bed; rm Pan5217_exomedepth.bed_unsorted.bed

## Gene list check
Check all genes in the bedfile request form are present in the final bedfile.

- Save Pan5217 request form (This was approved by Michael Yau)

1. Take a copy of Pan5211_exomedepth.bed 
    cp Pan5217_exomedepth.bed Pan5217_genecheck.csv

2. Open Pan5217_genecheck.csv use "_" to seperate gene name from exon number and delete the exon number column

3. Add header: Chr,Start,Stop,Gene

4. Create all transcript file; copy the genes and transcript list in the request form into an empty Excel file and save it as a CSV file

5. Run compare_genelists.py

python3 ~/Documents/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5217_genecheck.csv /home/natasha/Documents/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5217_alltranscripts.csv Gene Gene

Output: 
Genes missing:
{'HYCC1', 'GBA1', 'MTRFR'}

Troubleshooting
hycc1= FAM126A 
mtrfr = C12orf65
GBA1= GBA 

Script was run a second time to check addiotional genes present in data.bed which weren't requested

python3 ~/Documents/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Documents/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5217_alltranscripts.csv Pan5217_genecheck.csv Gene Gene

Genes missing:
{'CNV08', 'FAM126A', 'BRCA1-IN11-1', 'CNV12-1', 'CNV11', 'RNU4ATAC', 'CNV09-1', 'CNV16-1', 'BRCA1-PM-5-2', 'CNV13', 'CNV10-1', 'C12orf65', 'BRCA1-IN12-1', 'CNV02-1', 'BRCA1-IN11-2', 'CNV07', 'CNV15', 'BRCA1-PM-5-1', 'CNV03', 'BRCA1-PM-5-3', 'GBA', 'BRCA1-PM-5-4', 'CNV14-1', 'BRCA1-IN12-2'}

Regions highlighted are the additionally requested regions e.g CNV control sites, intronic regions
RNU4ATAC is an RNA gene not included in the request form but MYau confirmed the gene is required.

# Update request form

Add RNU4ATAC to the request form