## Pan5191
This VCP1 Exomedepth readcount BED file is based on Pan4398, 5UTR was included- no regions have been padded. 

Additional regions were included in this BED file:
Pan4291.bed- intronic variants relevant to Haematological genes
Pan4290.bed- intronic variants for VCP1 regions
Pan4292.bed- FH intronic variants padded by 5bp
Pan4272.bed- intronic variants for CF
Pan3608.bed- additional CNV regions

# Run Mokabed
Time Stamp:2023-10-10 10:41:41.354574
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5191dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5191.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5191data.bed --logfile /home/dnanexus/out/Output_files/Pan5191_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add regions from duplicate transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5191_duplicatesdata.bed -b Pan5191data.bed >> Pan5191data.bed

# Delete any unrequired files
rm Pan5191dataRefSeqFormat.txt Pan5191_duplicatesdataSambamba.bed Pan5191_duplicatesdataRefSeqFormat.txt Pan5191dataSambamba.bed Pan5191_duplicatesdata.bed Pan5191_duplicates_LogFile.txt

# Add in the additional panels.
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed Pan3608.bed >> Pan5191data.bed

# Sort data.bed
sort Pan5191data.bed -k1,1V -k2,2n -k3,3n > Pan5191data_sorted.bed; mv Pan5191data.bed Pan5191data_unsorted.bed; mv Pan5191data_sorted.bed Pan5191data.bed; rm Pan5191data_unsorted.bed

move header to the top

# Fix LAMA2 exon (without padding)
One of the LAMA2 exons was mapped incorrectly. The incorrect coordinates are: chr6:129763366-129763372 and the correct coordinates - chr6:129764207-129764213

# Testing
Pan5191data.bed was test using mokapicard, job completed without error.
Save request form

## Creating Exomedepth readcount BED file
1. Create a copy of Pan5191data.bed to make changes 
    cp Pan5191data.bed Pan5191_capture.bed

2. Replace Entrez IDs with gene symbols Open Pan5191_capture.bed in Excel, first split the GeneAccession column on semi colon and   create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab This helps visualise changes during code review

In Excel format Entrez;Gene_Accession to only include gene symbol:
a) Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

b) Step above left additionally added regions with empty cells in Gene_Accession column. Manually copy EntrezID field into Gene_accession column.

c) Delete Entrez ID column

4. Convert 4 column format 
    cut -f1-4 Pan5191_capture.bed > Pan5191data_4col.bed

5. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

6. Generate intermediary exomedepth files for exons TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5191 Pan5191data_4col.bed

7. Edit missing regions file (_Pan5191_missed.bed) strand information (BED6) Strand information obtained from Ensembl Diff performed in vscode between _Pan5191_missed.bed and Pan4398_extra.bed, no differences in shared regions

    - Simplify DMD region naming; replace description with DMD-INTRONIC

8. Regenerate (final) exomedepth files giving the additional non-exonic regions from last step 
TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5191_final Pan5191data_4col.bed _Pan5191_missed.bed

note after this stage there are no missed regions (Pan5191_final_missed.bed is empty)

9. Sort and rename final file 
    mv Pan5191_final_exomedepth.bed Pan5191_final_exomedepth_unsorted.bed; sort -k1,1V -k2n,3n Pan5191_final_exomedepth_unsorted.bed > Pan5191_final_exomedepth.bed; rm Pan5191_final_exomedepth_unsorted.bed

10. rename exome depth 
    git mv Pan5191_final_exomedepth.bed Pan5191_exomedepth.bed

# BEDtool subdtract
Bedtools substract was also perfomed on Pan5191_exomedepth.bed -b Pan5191_capture.bed, to identify any extra regions in Pan5191_exomedepth.bed.

bedtools subtract -A -a Pan5191_exomedepth.bed -b Pan5191data_4col.bed
AND
bedtools subtract -A -b Pan5191_exomedepth.bed -a Pan5191data_4col.bed

No differences were observed.

# Remove unrequired files
rm _Pan5191* Pan5191_final* Pan5191_capture.bed Pan5191data_4col.bed

# Testing 
Pan5191_exomedepth.bed was tested using DNANexus app ED_readcount_analysis_v1.0.0 in project 003_230627_Exomedepth_BEDfiles. The app completed sucessfully.
