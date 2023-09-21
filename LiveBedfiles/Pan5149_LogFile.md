This BED file is a remake of Pan4995, the VCP3 +/-30bp panel, but with the UTRs padded by +/-30bp

From past attempts of making this BED file there are additional steps required to create this BED file:
    1) SNORD118 gene is non-coding RNA, so doesn't have a NM number. Therefore must be added manually.
    2) LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected.
    3) SMN1 was found to be problematic therefore has to be done manually.
    4) Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database. Both transcripts were compared and no differences were found.

# Run mokabed for main transcript list and genes with multiple transcripts (Pan5149_extra.txt and Pan5149_extra_part1.txt)
Time Stamp:2023-09-08 11:22:26.325715
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5149dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --down 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5149.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5149data.bed --logfile /home/dnanexus/out/Output_files/Pan5149_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Combine duplicate transcripts

# merge Pan5149_extra_part1data.bed and Pan5149_extradata.bed
bedtools subtract -a Pan5149_extra_part1data.bed -b Pan5149_extradata.bed >> Pan5149_extradata.bed

# merge Pan5149_extradata_merged.bed with Pan5149data.bed
bedtools subtract -a Pan5149_extradata.bed -b Pan5149data.bed >> Pan5149data.bed

## Add SMN1 problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which was causing mokabed to fail on a previous iteration of this BED file (Pan5149). Mokabed was failing because cruzdb was returning multiple records for the same transcript.

As described in Pan3973_log.md a number of steps were performed to extract the regions from the UCSC table browser, remove the UTRs.
The SMN1 regions were paded by 10 bases as this was the requirement back then, however now regions are padded by 30bp. SMN1 regions will be padded by 20bp to be consisted with this bedfile (Pan5149). The SMN1 BED file was also converted to the expected format (12 columns). This was done for data.bed and were saved as Pan5149_SMN1problemdata.bed. 

1) Pan3973_problemdata.bed was downloaded from the git history at commit 982b443698 (https://github.com/moka-guys/mokabed/tree/982b443698683532c2a4a0032e0ae370742ad41a/LiveBedfiles)

    rename Pan3973_problemdata.bed to Pan5149_SMN1problemdata.bed before padding
        mv Pan3973_problemdata.bed Pan5149_SMN1problemdata.bed

2) Add padding
    a) convert file to 3 column format
        awk -F'\t' '{print $1 "\t" $2 "\t" $3}' Pan5149_SMN1problemdata.bed > Pan5149_SMN1_3col.bed

    b) padding
    The regions were padding +/-20bp as per those regions produced by MokaBED using the following python code:

    with open('/home/natasha/Desktop/mokabed/LiveBedfiles/Pan5149_SMN1_3col.bed','r') as bedfile:
        for line in bedfile.readlines():
            chr,start,stop=line.split("\t")
            print str(chr)+"\t" + str(int(start)-20) + "\t" + str(int(stop)+20)        

    c) In Excel Pan5149_SMN1_30padding.bed was used to update Pan5149_SMN1problemdata.bed to convert back into a 12 column format.

# add to data.bed
cat Pan5149_SMN1problemdata.bed >> Pan5149data.bed There was no header to remove

## Add SNORD118 
SNORD118 gene is non-coding RNA, so doesn't have a NM number. 
The UCSC and NCBI refeq databases were checked and NR_033294.2 wasn't in the databases used by MokaBED. therefore the BED file couldn't be made using Mokabed.

Coordinates for SNORD118 were retrieved from UCSC chr17:8076771-8076906
The regions were padded by -/+30bp to match the padding in Pan5149

# Manually update Pan4535data.bed
17  8076741 8076936 727676  SNORD118;NR_033294.2

## Fix LAMA2,DIAPH1 and NBEA
Errors were noticed where small exons had been mapped incorrectly in the UCSC refseq database. 
The coordinated were retrived from Pan4361. Please note Pan4361 was padded by =/-10bp and this BED file is padded by +/-30bp. LAMA2, DIAPH1 and NBEA regions were amended accordingly.

Three areas were identified: 
LAMA2;NM_000426.4
old - 6 129763336 129763402
new - 6 129764177 129764243

DIAPH1;NM_005219.5

old - 5 140915590 140915659
new - 5 140950964 140951033

NBEA;NM_015678.5
old - 13 35739200 35739265
new - 13 35739180 35743162

## Sort Pan5149data.bed
sort Pan5149data.bed -k1,1V -k2,2n -k3,3n > Pan5149data_sorted.bed; mv Pan5149data.bed Pan5149data_unsorted.bed; mv Pan5149data_sorted.bed Pan5149data.bed; rm Pan5149data_unsorted.bed

# move header to top

## Add intronic regions and CNV sites

Oops forgot to add the additional inronic regions and CNV sites

# Add Pan5167.bed
cat Pan5167.bed >> Pan5149data.bed

# Add Pan3608.bed
cat Pan3608.bed >> Pan5149data.bed

## check all trasncripts included
Added full list of transcripts included.
`bash /home/natasha/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/transcript_checker.sh /home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5149_all_transcripts.csv /home/natasha/Desktop/mokabed/LiveBedfiles/Pan5149data.bed`
output:
`Bed file as expected (all transcripts present)`

## Sort and rename again Pan5149data.bed
sort Pan5149data.bed -k1,1V -k2,2n -k3,3n > Pan5149data_sorted.bed; mv Pan5149data.bed Pan5149data_unsorted.bed; mv Pan5149data_sorted.bed Pan5149data.bed; rm Pan5149data_unsorted.bed

# move header to top

## Remove unrequired files
rm  Pan5149_extradata.bed Pan5149_extra_part1dataSambamba.bed Pan5149_SMN1_30padding.bed Pan5149dataRefSeqFormat.txt Pan5149_extradataRefSeqFormat.txt  Pan5149_extra_part1data.bed Pan5149_SMN1_3col.bed Pan5149dataSambamba.bed     Pan5149_extradataSambamba.bed Pan5149_extra_part1dataRefSeqFormat.txt Pan5149_SMN1problemdata.bed

## Testing
Pan5149data.bed was tested using moka_picard_v1.2.1 - job completed sucessfully

## Creating Exomedepth BED file
This BED file is used to do read count step of exome depth for CNV analysis of VCP3.

1. Create a copy of Pan5149data.bed to make changes
    cp Pan5149data.bed Pan5149_capture.bed

2. Replace Entrez IDs with gene symbols
    Open Pan5149_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating 
    EntrezID;GeneSymbol.
    Excel saves file as a csv, so open file in VS code and replace "," with a tab
    This helps visualise changes during code review

    In Excel format Entrez;Gene_Accession to only include gene symbol
    a) Use find and replace to edit Entrez;GeneSymbol column to only include Gene symbols.
                Find *; and and leave replace field empty (remember to select wildcard option)
                Excel saves output as csv, in VScode replace "," with a tab

    b) Step above left additionally added regions with empty cells in Gene_Accession column. Manually copy EntrezID field into      Gene_accession column.

    c) Delete Entrez ID column

3. Convert 4 column format
    Excel saves output as csv, in VScode replace "," with a tab
    cut -f1-4 Pan5149_capture.bed > Pan5149data_4col.bed

4. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

5. Generate intermediary exomedepth files for exons
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5149 Pan5149data_4col.bed

6. Edit missing regions file (_Pan5149_missed.bed)
    strand information (BED6)
    5th column was set to 0 6th column was set to + or -. Strand information was obtained from _Pan5149.bed, findstrand.py was used to join files using transcript numbers. 
    
    First update Pan5149_all_transcripts.csv to contain gene symbol column
    Add headers to Pan5149_all_transcripts.csv and _Pan5149_missed.bed- needed to run findstrand.py
    Convert _Pan5149.bed into 6 columns
        `cut -f 1-6  _Pan5149.bed > _Pan5149_6col.bed`
        Open _Pan5149_6col.bed in Excel, use "." as a seperator and add headers to file
    
    Run findstrand.py 
        python3 /home/natasha/Desktop/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/findstrand.py

    Rename output so its easier to track
    mv merged_file.csv Pan5149_merged_file.csv
    mv merged_file_final.csv Pan5149_merged_file_final.csv

    Open Pan5149_merged_file_final.csv in Excel and remove Transcript column as its not required

    Open file in vscode and replace "," with "\t"

    Remove header from Pan5149_merged_file_final.csv

    Rename file from .csv to .bed
        mv Pan5149_merged_file_final.csv _Pan5149_missing_updated.bed

7. Regenerate (final) exomedepth files giving the additional non-exonic regions from last step
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5149_final Pan5149data_4col.bed _Pan5149_missing_updated.bed

8. Pan5149_final_missed.bed was not empty, findstrand.py script could not find strand information for regions added from Pan5167.bed and Pan3608.bed.

    Strand information for this information was manually added. Strand information obtained from Ensembl
    NOTE: Mokabed named HYCC1 to its gene synonym FAM126A

9. Accidentally overwrote required file _Pan5149_missing_updated.bed.
    _Pan5149_missing_updated.bed downloaded from commit 3fbb917

10. Combine Pan5149_final_missed.bed and _Pan5149_missing_updated.bed
    cat Pan5149_final_missed.bed >> _Pan5149_missing_updated.bed

11. Sort and rename
    sort _Pan5149_missing_updated.bed -k1,1V -k2,2n -k3,3n > _Pan5149_missing_updated_sorted.bed; mv _Pan5149_missing_updated.bed _Pan5149_missing_updated_unsorted.bed; mv _Pan5149_missing_updated_sorted.bed _Pan5149_missing_updated.bed; rm _Pan5149_missing_updated_unsorted.bed