## Pan5208
This VCP1 Exomedepth readcount BED file it is a remake of Pan5191. LDLR and PCSK9 were accidentally excluded from the bed file. Pan5206 will have up and down coding regions included and the 5UTR - no regions have been padded.

Additional regions were included in this BED file: 
Pan4291.bed- intronic variants relevant to Haematological genes 
Pan4290.bed- intronic variants for VCP1 regions 
Pan4292.bed- FH intronic variants padded by 5bp Pan4272.bed- intronic variants for CF 
Pan3608.bed- additional CNV regions

# Save transcript files

# Run mokabed
Time Stamp:2024-02-23 11:52:18.863593
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5208dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5208.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5208data.bed --logfile /home/dnanexus/out/Output_files/Pan5208_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add regions from extra transcripts to data.bed
Use bedtools subtract to add regions from extra transcripts that aren't in main file.

bedtools subtract -a Pan5208_extradata.bed -b Pan5208data.bed >> Pan5208data.bed

# Add additional panels
cat Pan4291.bed Pan4290.bed Pan4292.bed Pan4272.bed Pan3608.bed >> Pan5208data.bed

# Sort data.bed
sort Pan5208data.bed -k1,1V -k2,2n -k3,3n > Pan5208data_sorted.bed; mv Pan5208data.bed Pan5208data_unsorted.bed; mv Pan5208data_sorted.bed Pan5208data.bed; rm Pan5208data_unsorted.bed

Move header to the top

# Fix LAMA2 exon (without padding)
One of the LAMA2 exons was mapped incorrectly. The incorrect coordinates are: chr6:129763366-129763372 and the correct coordinates - chr6:129764207-129764213

# Check all requested genes present 

a) Take a copy of Pan5208data.bed to convert into a 6 column bed file.
    cp Pan5208data.bed Pan5208data_6col.csv

b) Open Pan5208data_6col.csv in Excel, separating the GeneAccession column on “;” and delete empty columns between EntrezID column  and GeneAccession column

c) Delete first row, contains date e.g #2023-10-10 10:41:52.716212

d) Rename header to: Chr, Start, Stop, EntrezID, Gene, Transcript

e) Create second input file; copy the genes and transcript list in the request form into an empty Excel file and save it as a CSV file

f) Add headers to columns: Gene, Transcript

g) Run compare_genelists.py

First check if any genes are missing in the data.bed file

    python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5208data_6col.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5208_alltranscripts.csv Gene Gene

NOTE: Output showed no genes were missing

Script was run a second time to check addiotional genes present in data.bed which weren't requested

    python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5208_alltranscripts.csv Pan5208data_6col.csv Gene Gene

NOTE: Output showed no additional genes were present

# Delete unrequired files

rm Pan5208data_6col.csv Pan5208dataRefSeqFormat.txt Pan5208dataSambamba.bed Pan5208_extradata.bed Pan5208_extradataRefSeqFormat.txt Pan5208_extradataSambamba.bed

# Testing
Pan5208data.bed was test using mokapicard, job completed without error. Save request form

############################################################################################################################
Exomedepth Readcount BED file
############################################################################################################################

# Copy data.bed
Take a copy of the data.bed file, any changes will be made to the copy of data.bed and not the original

cp Pan5208data.bed Pan5208_capture.bed

# Replace Entrez ID with gene symbols

a) Open Pan5191_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab This helps visualise changes during code review

In Excel format Entrez;Gene_Accession to only include gene symbol: 
b) Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

NOTE: Noticed the concatenation didn't apply for majority of the regions, so starting from step A again.

Repeat step B (find and replace)

c) Step above left additionally added regions with empty cells in GeneSymbol column. Manually copy EntrezID field into GeneSymbol column.

d) Delete Entrez ID column

# Convert 4 column format 
cut -f1-4 Pan5208_capture.bed > Pan5208data_4col.bed

# Replace underscores
Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

Noticed 7:117179036-117179049 had a missing GeneSymbol column, fix that by adding rs397508809 to the cell

# Run makeExomedepth.sh
Generate intermediary exomedepth files for exons TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5208 Pan5208data_4col.bed

# Edit missing regions file
Edit missing regions file (_Pan5208_missed.bed) strand information (BED6) Strand information obtained from Ensembl 
Diff performed in vscode between _Pan5208_missed.bed and _Pan5191_missed.bed, no differences in shared regions.

Simplify DMD region naming; replace description with DMD-INTRONIC

# Rerun makeExomedepth.sh
Regenerate (final) exomedepth files giving the additional non-exonic regions from last step TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5208_final Pan5208data_4col.bed _Pan5208_missed.bed

Check if Pan5208_final_missed.bed is empty, before proceeding.

# Sort and rename
mv Pan5208_final_exomedepth.bed Pan5208_final_exomedepth_unsorted.bed; sort -k1,1V -k2n,3n Pan5208_final_exomedepth_unsorted.bed > Pan5208_final_exomedepth.bed; rm Pan5208_final_exomedepth_unsorted.bed

# rename exome depth 
git mv Pan5208_final_exomedepth.bed Pan5208_exomedepth.bed