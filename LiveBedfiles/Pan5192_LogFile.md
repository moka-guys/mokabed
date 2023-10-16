This VCP3 BED file is a remake of Pan5149, but with no padding to the exons and only the 5 UTR included.

From past attempts of making this BED file there are additional steps required to create this BED file: 
    - SNORD118 gene is non-coding RNA, so doesn't have a NM number. Therefore must be added manually.
    - LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected.
    - SMN1 was found to be problematic therefore has to be done manually.
    - Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database. Both transcripts were compared and no differences were found.

# Run mokabed
Time Stamp:2023-10-16 13:49:04.986853
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5192dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5192.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5192data.bed --logfile /home/dnanexus/out/Output_files/Pan5192_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Combine duplicate transcripts
merge Pan5192_extra_part1data.bed and Pan5192_extradata.bed

bedtools subtract -a Pan5192_extra_part1data.bed -b Pan5192_extradata.bed >> Pan5192_extradata.bed

merge Pan5192_extradata_merged.bed with Pan5192data.bed
bedtools subtract -a Pan5192_extradata.bed -b Pan5192data.bed >> Pan5192data.bed

# Add SMN1 problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which was causing mokabed to fail on a previous iteration of this BED file (Pan5192). Mokabed was failing because cruzdb was returning multiple records for the same transcript.

As described in Pan3973_log.md a number of steps were performed to extract the regions from the UCSC table browser, remove the UTRs. The SMN1 regions were padded by 10 bases as this was the requirement back then, however now no padding is added to regions. SMN1 regions 10bp padding will be removed to be consisted with this bedfile (Pan5192). The SMN1 BED file was also converted to the expected format (12 columns). This was done for data.bed and was saved as Pan5192_SMN1problemdata.bed.

1. Pan3973_problemdata.bed was downloaded from the git history at commit 982b443698 (https://github.com/moka-guys/mokabed/tree/982b443698683532c2a4a0032e0ae370742ad41a/LiveBedfiles)

2. rename Pan3973_problemdata.bed to Pan5192_SMN1problemdata.bed before removing padding 
mv Pan3973_problemdata.bed Pan5192_SMN1problemdata.bed

3. Remove padding 
    a) convert file to 3 column format awk -F'\t' '{print $1 "\t" $2 "\t" $3}' Pan5192_SMN1problemdata.bed > Pan5192_SMN1_3col.bed

    b) 10bp was removed, as per those regions produced by MokaBED using the following python code:
        with open('/home/natasha/Desktop/mokabed/LiveBedfiles/Pan5192_SMN1_3col.bed','r') as bedfile: for line in bedfile.readlines(): chr,start,stop=line.split("\t") print str(chr)+"\t" + str(int(start)+10) + "\t" + str(int(stop)-10)

    c) In Excel Pan5192_SMN1_nopadding.bed was used to update Pan5192_SMN1problemdata.bed to convert back into a 12 column format.

# add to data.bed
cat Pan5192_SMN1problemdata.bed >> Pan5192data.bed There was no header to remove

# Add SNORD118
SNORD118 gene is non-coding RNA, so doesn't have a NM number. The UCSC and NCBI refeq databases were checked and NR_033294.2 wasn't in the databases used by MokaBED. therefore the BED file couldn't be made using Mokabed.

Coordinates for SNORD118 were retrieved from UCSC chr17:8076771-8076906. No padding was added to these regions

# Fix LAMA2,DIAPH1 and NBEA
Errors were noticed where small exons had been mapped incorrectly in the UCSC refseq database. The coordinated were retrived from Pan4361. Please note Pan4361 was padded by +/-10bp and this BED file has no padding. 10bp padding was removed from LAMA2, DIAPH1 and NBEA regions

Three areas were identified: 
LAMA2;NM_000426.4 
old - 6 129763366-129763372 new - 6	129764197-129764213

DIAPH1;NM_005219.5

old - 5	140915620-140915629 new - 5	140950984-140951013


NBEA;NM_015678.5 
old - 13 35739230-35739235 new - 13 35739190-35743152

Sort Pan5192data.bed
sort Pan5192data.bed -k1,1V -k2,2n -k3,3n > Pan5192data_sorted.bed; mv Pan5192data.bed Pan5192data_unsorted.bed; mv Pan5192data_sorted.bed Pan5192data.bed; rm Pan5192data_unsorted.bed

# move header to top

# Add intronic regions and CNV sites
Oops forgot to add the additional inronic regions and CNV sites

cat Pan5167.bed Pan3608.bed >> Pan5192data.bed

# check all trasncripts included
Added full list of transcripts included. 
bash /home/natasha/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/transcript_checker.sh /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5192_all_transcripts.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Pan5192data.bed 
output: Bed file as expected (all transcripts present)

# Sort and rename again Pan5192data.bed
sort Pan5192data.bed -k1,1V -k2,2n -k3,3n > Pan5192data_sorted.bed; mv Pan5192data.bed Pan5192data_unsorted.bed; mv Pan5192data_sorted.bed Pan5192data.bed; rm Pan5192data_unsorted.bed

# move header

# Remove unrequired files
rm Pan5192_extradata.bed Pan5192_extra_part1dataSambamba.bed Pan5192_SMN1_nopadding.bed Pan5192dataRefSeqFormat.txt Pan5192_extradataRefSeqFormat.txt Pan5192_extra_part1data.bed Pan5192_SMN1_3col.bed Pan5192dataSambamba.bed Pan5192_extradataSambamba.bed Pan5192_extra_part1dataRefSeqFormat.txt Pan5192_SMN1problemdata.bed

# Testing
Pan5192data.bed was tested using moka_picard_v1.2.1 - job completed sucessfully