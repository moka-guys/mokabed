## Pan5188
This VCP2 BED file is based on Pan5119, 5UTR was included- no regions have been padded.

# Run mokabed
Time Stamp:2023-10-10 10:51:37.957122
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5188dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5188.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5188data.bed --logfile /home/dnanexus/out/Output_files/Pan5188_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Add additional regions
NOTE: Pan4283 no longer added as entire CHEK2 gene now included and BRAC1 UTRs are included, therefore all regions in Pan4283 are covered.

cat Pan5117.bed Pan3610.bed Pan3608.bed >> Pan5188data.bed

# Sort Pan5188data.bed
sort Pan5188data.bed -k1,1V -k2,2n -k3,3n > Pan5188data_sorted.bed; mv Pan5188data.bed Pan5188data_unsorted.bed; mv Pan5188data_sorted.bed Pan5188data.bed; rm Pan5188data_unsorted.bed

move header to the top manually

# delete intermediate/incomplete files
rm Pan5188dataRefSeqFormat.txt Pan5188dataSambamba.bed

# Testing
Pan5188data.bed was tested using moka_picard_v1.2.1 - job completed sucessfully

## Creating Exomedepth BED file
This BED file is used to do read count step of exome depth for CNV analysis of VCP2.

1. Create a copy of Pan5188data.bed to make changes
    cp Pan5188data.bed Pan5188_capture.bed

2. Replace Entrez IDs with gene symbols
    Open Pan5188_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating 
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
    cut -f1-4 Pan5188_capture.bed > Pan5188data_4col.bed

4. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

5. Generate intermediary exomedepth files for exons
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5188 Pan5188data_4col.bed

6. Edit missing regions file (_Pan5188_missed.bed) strand information (BED6) 5th column was set to 0 6th column was set to + or -. This was taken from _Pan4973_missed.bed. The GREM1_SCG5 regions were given set to + since both genes are on the forward strand. CHEK2,TP53 set to - as gene is on reverse strand Strand information obtained from Ensembl Diff performed in vscode between _Pan5188_missed.bed and _Pan4973_missed.bed, no differences in shared regions.

    NOTE: fix the naming of the GREM1_SCG5 intronic regions. It doesn't need to have the additional details.

7. Regenerate (final) exomedepth files giving the additional non-exonic regions from last step 
TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5188_final Pan5188data_4col.bed _Pan5188_missed.bed

note after this stage there are no missed regions (Pan5188_final_missed.bed is empty)

8. Sort and rename
mv Pan5188_final_exomedepth.bed Pan5188_final_exomedepth_unsorted.bed; sort -k1n,1 -k2n,3n Pan5188_final_exomedepth_unsorted.bed > Pan5188_final_exomedepth.bed; rm Pan5188_final_exomedepth_unsorted.bed

9. rename exome depth git mv Pan5188_final_exomedepth.bed Pan5188_exomedepth.bed

10. remove intermediate files rm _Pan5188* Pan5188_final*

# Fix naming
It was noticed few regions had two labels i.e ARHGAP11A-SCG5,SCG5_1. This was caused due to duplicate regions in Pan5117.bed, Pan3610.bed and Pan3608.bed. 

# Testing
 Pan5144_exomedepth.bed was tested using DNANexus app ED_readcount_analysis_v1.0.0 in project 003_230627_Exomedepth_BEDfiles. The app completed sucessfully.

Bedtools substract was also perfomed on Pan5188_exomedepth.bed -b Pan5188_capture.bed, to identify any extra regions in Pan5188_exomedepth.bed.

bedtools subtract -A -a Pan5188_exomedepth.bed -b Pan5188_capture.bed

# remove intermediate files 
rm Pan5188_capture.bed Pan5188data_4col.bed