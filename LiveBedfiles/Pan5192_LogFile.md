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

## NOTE: THESE (LAMA2, DIAPH1 and NBEA) REGIONS WERE UPDATED INCORRECTLY, SEE END OF LOGFILE!!
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

## Creating Exomedepth BED file
This BED file is used to do read count step of exome depth for CNV analysis of VCP3.

1. Create a copy of Pan5192data.bed to make changes 
cp Pan5192data.bed Pan5192_capture.bed

2. Replace Entrez IDs with gene symbols Open Pan5192_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab This helps visualise changes during code review
    a) In Excel format Entrez;Gene_Accession to only include gene symbol a) Use find and replace to edit Entrez;GeneSymbol column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

    b) Step above left additionally added regions with empty cells in Gene_Accession column. Manually copy EntrezID field into Gene_accession column.

3. Convert 4 column format Excel saves output as csv, in VScode replace "," with a tab 
    cut -f1,2,3,5 Pan5192_capture.bed > Pan5192data_4col.bed

4. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

5. Generate intermediary exomedepth files for exons TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5192 Pan5192data_4col.bed

6. Edit missing regions file (_Pan5192_missed.bed) strand information (BED6) 5th column was set to 0 6th column was set to + or -. Strand information was obtained from _Pan5192.bed, findstrand.py was used to join files using transcript numbers.

    - Add headers to _Pan5192_missed.bed- needed to run findstrand.py 

    - Convert _Pan5192.bed into 6 columns
      cut -f 1-6  _Pan5192.bed > _Pan5192_6col.bed 
      Open _Pan5192_6col.bed in Excel, use "." as a seperator and add headers to file

7. Run findstrand.py python3 /home/natasha/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/findstrand.py

8. Open Pan5192_merged_file_final.csv in Excel and remove Transcript column as its not required

    - Open file in vscode and replace "," with "\t"

    - Remove header from Pan5192_merged_file_final.csv

    - Rename file from .csv to .bed mv Pan5192_merged_file_final.csv _Pan5192_missing_updated.bed

    - Remove transcript version column

9. Regenerate exomedepth files giving the additional non-exonic regions from last step TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5192_part1 Pan5192data_4col.bed _Pan5192_missing_updated.bed

## Running into exomedepth.sh errors, redoing from step 9

10. Pan5192_part1_missed.bed was not empty, findstrand.py script could not find strand information for regions added from Pan5167.bed and Pan3608.bed.
    Strand information for this information was manually added. Strand information obtained from Ensembl NOTE: Mokabed named HYCC1 to its gene synonym FAM126A

11. Combine Pan5192_part1_missed.bed and _Pan5192_missing_updated.bed cat Pan5192_part1_missed.bed >> _Pan5192_missing_updated.bed

12. Sort and rename sort _Pan5192_missing_updated.bed -k1,1V -k2,2n -k3,3n > _Pan5192_missing_updated_sorted.bed; mv _Pan5192_missing_updated.bed _Pan5192_missing_updated_unsorted.bed; mv _Pan5192_missing_updated_sorted.bed _Pan5192_missing_updated.bed; rm _Pan5192_missing_updated_unsorted.bed

13. Duplicate SNORD118 region (17:8076741-8076936) present without strand information. Delete the line without info.

14. Rerun exomedepth script TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5192_final Pan5192data_4col.bed _Pan5192_missing_updated.bed

Pan5192_final_missed.bed should now be empty

15. Rename exome depth git mv Pan5192_final_exomedepth.bed Pan5192_exomedepth.bed

16. Delete unrequired files rm _Pan5192* Pan5192_part1* Pan5192_final*

17. Pan5192_exomedepth.bed was tested using DNANexus app ED_readcount_analysis_v1.1.0 in project 230822_VCP3_exomedepth_bedfiles. App completed successfully

18. Delete further unrequired files rm Pan5192_capture.bed Pan5192data_4col.bed merged_file.csv

# During codereview it was noted LAMA2;NM_000426.4 and NBEA;NM_015678.5 region was not corrected
EDIT Pan5192data.bed and Pan5192_exomedepth.bed
LAMA2 start position was padded by -/+10bp
LAMA2 6:129764197-129764213 corrected to 6:129764207-129764213

DIAPH1;NM_005219.5 nothing needs to be changed.
correct coordinates without padding are 5:140950994-140951003

NBEA;NM_015678.5 
Pan5192_exomedepth.bed
old - 13 35739230-35739235 
new - 13 35743123-35743132

Pan5192data.bed
incorrect 13:35739190-35743152
correct: 13:35743123-35743132


# Testing
Bedtools substract was also perfomed on Pan5192_exomedepth.bed -b Pan5192_capture.bed (4 column format), to identify any extra regions in Pan5192_exomedepth.bed.

bedtools subtract -A -a Pan5192_exomedepth.bed -b Pan5192data_4col.bed AND bedtools subtract -A -b Pan5192_exomedepth.bed -a Pan5192data_4col.bed

No differences were observed.

Pan5192_exomedepth.bed was tested again using DNANexus app ED_readcount_analysis_v1.0.0 in project 003_230627_Exomedepth_BEDfiles. The app completed sucessfully.

# Make changes identifies in the PR
Fix LAMA, NBEA regions
Correct request form

# Test changes
Pan5192_exomedepth.bed tested in 003_231117_exomedepth_apps_v1.3.0 using ED_readcount_analysis_v1.3.0 and ED_cnv_calling_v1.3.0
The apps completed successfully