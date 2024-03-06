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