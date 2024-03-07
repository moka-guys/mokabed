# Pan5211
This VCP3 BED file is a remake of Pan5192, few requested genes(DOLK,FANCF,NHLRC1,PRKACG,RNF113A,THBD,RNU4ATAC) were found to be missing from Pan5192.

From past attempts of making this BED file there are additional steps required to create this BED file: -
 - SNORD118 and RNU4ATAC genes are non-coding RNA, so don't have a NM number. Therefore must be added manually. 
 - LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected. 
 - SMN1 was found to be problematic therefore has to be done manually.
 - Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database.   Both transcripts were compared and no differences were found.

 # Create Transcript files
For few genes multiple transcript have been requested, these were separated into Pan5211.txt, Pan5211_part1.txt, and Pan5211_part2.txt

# Run Mokabed
Time Stamp:2024-02-28 11:58:14.098253
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5211dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5211.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5211data.bed --logfile /home/dnanexus/out/Output_files/Pan5211_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Combine multiple transcripts
merge Pan5211_part1data.bed and Pan5211_part2data.bed

bedtools subtract -a Pan5211_part2data.bed -b Pan5211_part1data.bed  >> Pan5211_part1data.bed

merge Pan5211_part1data.bed with Pan5211data.bed 

bedtools subtract -a Pan5211_part1data.bed -b Pan5211data.bed >> Pan5211data.bed

# Fix missing genes

From previous iterations of making this BEDfile we noticed Mokabed excludes certain genes from its output, to obtain a conclusive list of missing genes, compare_genelists.py was run

a) Take a copy of Pan5211ata.bed to convert into a 6 column csv file.
    cp Pan5211data.bed Pan5211data_6col.csv

b) Open Pan5211data_6col.csv in Excel, separating the GeneAccession column on “;” and delete empty columns between EntrezID column and Gene column

c) Delete first row, contains date e.g #2023-10-10 10:41:52.716212

d) Rename header to: Chr, Start, Stop, EntrezID, Gene, Transcript

e) Prepare the second input; copy the genes and transcript list in the request form into an empty Excel file and save it as a CSV file

f) Add headers to columns: Gene, Transcript

g) Run the script:
    
    python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5211data_6col.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Gene Gene

    Script output:
   Genes missing: {'RNF113A', 'RNU4ATAC', 'NHLRC1', 'PRKACG', 'FANCF', 'SNORD118', 'SMN1', 'THBD', 'DOLK'}

 The script was run again to check for additional genes in Pan5211data_6col.csv
     python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Pan5211data_6col.csv Gene Gene

     No additional genes found

h) The output from compare_genelists.py was investigated:
    'RNF113A'= Not included by mokabed
    'RNU4ATAC' = Will be manually included since its an RNA gene
    'NHLRC1'=  Not included by mokabed
    'PRKACG'= Not included by mokabed
    'FANCF'= Not included by mokabed
    'SNORD118'= Will be manually included since its an RNA gene
    'SMN1'= Problematic with mokabed will be included manually.
    'THBD'= Not included by mokabed
    'DOLK'= Not included by mokabed

# Add missing genes bed file
MokaBED fails to add certain single exon genes in the data.bed output, padding the genes didn’t solve the issue. A seperate bedfile (Pan5213) for: RNF113A, NHLRC1, PRKACG, FANCF, THBD, and DOLK was manually created and this will be merged with Pan5211data.bed

Please see https://github.com/moka-guys/mokabed/blob/master/LiveBedfiles/Pan5213_LogFile.md for further details on how this bedfile was created.

cat Pan5213.bed >> Pan5211data.bed

# Add SMN1 problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which is known to cause mokabed to fail on a previous iterations. Mokabed was failing because cruzdb was returning multiple records for the same transcript.

As described in Pan3973_log.md a number of steps were performed to extract the regions from the UCSC table browser, remove the UTRs. The SMN1 regions were padded by 10 bases as this was the requirement back then, however now no padding is added to regions. SMN1 regions 10bp padding will be removed to be consisted with this bedfile (Pan5211). The SMN1 BED file was also converted to the expected format (12 columns). This was done for data.bed and was saved as Pan5211_SMN1problemdata.bed.

1) Pan3973_problemdata.bed was downloaded from the git history at commit 982b443698 (https://github.com/moka-guys/mokabed/tree/982b443698683532c2a4a0032e0ae370742ad41a/LiveBedfiles)

2) Rename Pan3973_problemdata.bed to Pan5211_SMN1problemdata.bed before removing padding 
    mv Pan3973_problemdata.bed Pan5211_SMN1problemdata.bed

3) Remove padding 
    a) convert file to 3 column format awk -F'\t' '{print $1 "\t" $2 "\t" $3}' Pan5211_SMN1problemdata.bed > Pan5211_SMN1_3col.bed

    b) 10bp was removed, as per those regions produced by MokaBED using the following python code: with open('/home/natasha/Desktop/mokabed/LiveBedfiles/Pan5211_SMN1_3col.bed','r') as bedfile: for line in bedfile.readlines(): chr,start,stop=line.split("\t") print str(chr)+"\t" + str(int(start)+10) + "\t" + str(int(stop)-10)

    c) In Excel Pan5211_SMN1_3col.bed was used to update Pan5211_SMN1problemdata.bed to convert back into a 12 column format.

# add to data.bed
cat Pan5211_SMN1problemdata.bed >> Pan5211data.bed 
There was no header to remove

# Add SNORD118 and RNU4ATAC
SNORD118 and RNU4ATAC are non-coding RNA genes, so doesn't have a NM number, therefore the BED file couldn't be made using Mokabed.

Coordinates for SNORD118 and RNU4ATAC were retrieved from UCSC. No padding was added to these regions
SNORD118 chr17:8076770 - 8076906
RNU4ATAC chr2: 122288456-122288585

# Fix LAMA2, DIAPH1 and NBEA

Errors were noticed where small exons had been mapped incorrectly in the UCSC refseq database. The coordinates were retrived from Pan4361. Please note Pan4361 was padded by +/-10bp and this BED file has no padding. 10bp padding was removed from LAMA2, DIAPH1 and NBEA regions

LAMA2
incorrect 6:129763366-129763372
correct 6:129764207-129764213

DIAPH1
incorrect 5:140915620-140915629
correct 5:140950994-140951003

NBEA
incorrect 13:35739230-35739235
correct 13:35743123-35743132

# Sort and rename

sort Pan5211data.bed -k1,1V -k2,2n -k3,3n > Pan5211data_sorted.bed; mv Pan5211data.bed Pan5211data_unsorted.bed; mv Pan5211data_sorted.bed Pan5211data.bed; rm Pan5211data_unsorted.bed

move header to the top

# Add intronic regions and CNV sites
Oops forgot to add the additional inronic regions and CNV sites

cat Pan5167.bed Pan3608.bed >> Pan5211data.bed

# sort and rename again 

sort Pan5211data.bed -k1,1V -k2,2n -k3,3n > Pan5211data_sorted.bed; mv Pan5211data.bed Pan5211data_unsorted.bed; mv Pan5211data_sorted.bed Pan5211data.bed; rm Pan5211data_unsorted.bed

move header

# Check all requested genes are present

a) Take a copy of Pan5211data.bed to convert into a 6 column bed file. 
    cp Pan5211data.bed Pan5211data_6col.csv

b) Open Pan5211data_6col.csv in Excel, separating the GeneAccession column on “;” and delete empty columns between EntrezID column and GeneAccession column

c) Delete first row, contains date e.g #2023-10-10 10:41:52.716212

d) Rename header to: Chr, Start, Stop, EntrezID, Gene, Transcript

e) Second input file already exists, run compare_genelists.py
    First check if any genes are missing in the data.bed file
        python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5211data_6col.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Gene Gene

    NOTE: Output showed no genes were missing

    Script was run a second time to check addiotional genes present in data.bed which weren't requested
        python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Pan5211data_6col.csv Gene Gene

    NOTE: Output showed no genes were missing

# Delete unrequired files

rm Pan5211data_6col.csv Pan5211dataRefSeqFormat.txt Pan5211dataRefSeqFormat.txt Pan5211dataRefSeqFormat.txt Pan5211_part1data.bed Pan5211_part1dataRefSeqFormat.txt Pan5211_part1dataSambamba.bed Pan5211_part2data.bed Pan5211_part2dataRefSeqFormat.txt Pan5211_part2dataSambamba.bed Pan5211_SMN1_3col.bed Pan5211_SMN1problemdata.bed

# Testing
Pan5211data.bed was test using mokapicard, job completed without error.

#####################################################
# **Creating Exomedepth BED file**
######################################################

# Create a copy of Pan5211data.bed to make changes 
    cp Pan5211data.bed Pan5211_capture.bed

# Replace Entrez ID with gene symbols

a) Open Pan5211_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab This helps visualise changes during code review

b) In Excel format Entrez;Gene_Accession to only include gene symbol.
 Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

c) Step above left additionally added regions with empty cells in GeneSymbol column. Manually copy EntrezID field into GeneSymbol column.

d) Delete Entrez ID column

# Convert 4 column format
cut -f1-4 Pan5211_capture.bed > Pan5211data_4col.bed

# Replace underscores
Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

# Run makeExomedepth.sh
Generate intermediary exomedepth files for exons 
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5211 Pan5211data_4col.bed

# Edit missing regions file
Edit missing regions file (_Pan5211_missed.bed) strand information (BED6) 5th column was set to 0 6th column was set to + or -. Strand information was obtained from _Pan5211.bed, findstrand.py was used to join files using transcript numbers.

    - Add headers (chr,start,stop,Gene) to _Pan5211_missed.bed- needed to run findstrand.py

    - Convert _Pan5211.bed into 6 columns 
        cut -f 1-6 _Pan5211.bed > _Pan5211_6col.bed
        Open _Pan5211_6col.bed in Excel, use "." as a seperator and add headers to file

# Run findstrand.py 
    python3 /home/natasha/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/findstrand.py

# Remove transcript file
Open Pan5211_merged_file_final.csv in Excel and remove Transcript column as its not required

- Open file in vscode and replace "," with "\t"

- Remove header from Pan5211_merged_file_final.csv

# Rename file
- Rename file from .csv to .bed 
    mv Pan5211_merged_file_final.csv _Pan5211_missing_updated.bed

# Remove transcript version column

# Rerun makeExomedepth.sh
Regenerate exomedepth files giving the additional non-exonic regions from last step 
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5211_part1 Pan5211data_4col.bed _Pan5211_missing_updated.bed

# Manually update missing strand info
Pan5211_part1_missed.bed was not empty, findstrand.py script could not find strand information for regions added from Pan5167.bed and Pan3608.bed. 
Strand information for this information was manually added. Strand information obtained from Ensembl.

# Combine missing strand info files
    cat Pan5211_part1_missed.bed >> _Pan5211_missing_updated.bed

# Delete duplicate regions

Duplicate SNORD118 regions (17:8076741-8076936) and RNU4ATAC (2:122288456-122288585) present without strand information. Delete the lines without info.

# Sort and rename
sort _Pan5211_missing_updated.bed -k1,1V -k2,2n -k3,3n > _Pan5211_missing_updated_sorted.bed; mv _Pan5211_missing_updated.bed _Pan5211_missing_updated_unsorted.bed; mv _Pan5211_missing_updated_sorted.bed _Pan5211_missing_updated.bed; rm _Pan5211_missing_updated_unsorted.bed

# Rerun makeExomedepth.sh
TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5211_final Pan5211data_4col.bed _Pan5211_missing_updated.bed

Pan5211_final_missed.bed should now be empty

# Rename exomedepth file

    git mv Pan5211_final_exomedepth.bed Pan5211_exomedepth.bed

# Delete unrequired files
rm _Pan5211* Pan5211_part1* Pan5211_final*

# Final gene list check
Check all requested genes present in the exomedepth bed file

1. Take a copy of Pan5211_exomedepth.bed 
        cp Pan5211_exomedepth.bed Pan5211_genecheck.csv

2. Open Pan5211_genecheck.csv use "_" to seperate gene name from exon number and delete the exon number column

3. Add header: Chr,Start,Stop,Gene

4. Run compare_genelists.py

First check if any genes are missing in the data.bed file

    python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5211_genecheck.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Gene Gene

NOTE: Output showed no genes were missing

Script was run a second time to check additional genes present in data.bed which weren't requested

    python3 ~/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv Pan5211_genecheck.csv Gene Gene

NOTE: Output showed the additional regions were from CNV control site and intronic regions. Additionally 5 genes (COL4A2-AS2,LURAP1,METTL8,BIVM-ERCC5,INSRR) were also highlighted.
Genes missing:
{'BRCA1-IN11-1', 'COL4A2-AS2', 'BRCA1-PM-5-3', 'LURAP1', 'CNV12-1', 'METTL8', 'CNV14-1', 'CNV11', 'CNV15', 'BRCA1-IN12-2', 'CNV03', 'BIVM-ERCC5', 'CNV13', 'CNV16-1', 'CNV07', 'CNV08', 'INSRR', 'BRCA1-IN12-1', 'BRCA1-PM-5-2', 'BRCA1-IN11-2', 'CNV09-1', 'BRCA1-PM-5-1', 'BRCA1-PM-5-4', 'CNV10-1', 'CNV02-1'}

# Fix extra genes

compare_genelists.py identified 5 genes were extra in the final exomedepth bedfile. Upon investigation, these genes were included by the makeExomedepth.sh

LURAP1 (1:46685370-46685892) overlaps with POMGNT1_1. The gene name and the exon numbering was manually updated.

BIVM-ERCC5- was added as an additional label along with ERCC5. The additional label was removed

METTL8: 2:172291183-172291191 was included in the bed file because it overlapped with DCAF17_1. Since METTL8 is not required in VCP3, the overlapping region was removed. 

COL4A2-AS2 (13:111109120-111109703) is an RNA gene and part of it overlaps with COL4A2_21. COL4A2-AS2 is not required in VCP3, therefore it was manually removed.

INSRR (1:156811903-156812063) was included in the bed file because it overlapped with NTRK1_2. Since INSRR is not required in VCP3, the overlapping region was removed. 