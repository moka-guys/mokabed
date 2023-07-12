This BED file is a remake of Pan5119, the VCP2 +/-30bp panel, but with the UTRs padded by +/-30bp

## Run mokabed
Time Stamp:2023-07-11 10:37:07.733824
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5132dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --down 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5132.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5132data.bed --logfile /home/dnanexus/out/Output_files/Pan5132_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add additional regions
NOTE: Pan4283 no longer added as entire CHEK2 gene now included and BRAC1 UTRs padded by 30bp, therefore all regions in Pan4283 are covered.

# Add Pan5117
cat Pan5117.bed >> Pan5132data.bed

# Add Pan3610
cat Pan3610.bed >> Pan5132data.bed

# Add Pan3608
cat Pan3608.bed >> Pan5132data.bed

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
    Open Pan5132_capture.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating 
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
    Excel saves output as csv, in VScode replace "," with a tab
    cut -f1-4 Pan5132_capture.bed > Pan5132data_4col.bed

4. Underscores create issues with makeexomdepth.sh script, so in VScode replace any underscores with dashes.

5. Generate intermediary exomedepth files for exons
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan5132 Pan5132data_4col.bed

6. Edit missing regions file (_Pan5132_missed.bed)
    strand information (BED6)
    5th column was set to 0 6th column was set to + or -. This was taken from _Pan4973_missed.bed.
    The GREM1_SCG5 regions were given set to + since both genes are on the forward strand.
    CHEK2,TP53 set to - as gene is on reverse strand 
    Strand information obtained from Ensembl
    Diff performed in vscode between _Pan5132_missed.bed and _Pan4973_missed.bed, no differences in shared regions

7. Regenerate (final) exomedepth files giving the additional non-exonic regions from last step
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan5132_final Pan5132data_4col.bed _Pan5132_missed.bed

    - note after this stage there are no missed regions (Pan5132_final_missed.bed is empty)

8. Sort and rename final file
    mv Pan5132_final_exomedepth.bed Pan5132_final_exomedepth_unsorted.bed; sort -k1n,1 -k2n,3n Pan5132_final_exomedepth_unsorted.bed > Pan5132_final_exomedepth.bed; rm Pan5132_final_exomedepth_unsorted.bed

9. rename exome depth
    git mv Pan5132_final_exomedepth.bed Pan5132_exomedepth.bed

10. remove intermediate files
    rm _Pan5132* Pan5132_final*

11. Testing
    Pan5132_exomedepth.bed was tested using DNANexus app `ED_readcount_analysis_v1.0.0` in project 003_230627_Exomedepth_BEDfiles.
    The app completed sucessfully.

12. remove intermediate files
    rm Pan5132_capture.bed Pan5132data_4col.bed

## Fix multiple naming
It was noticed few regions had two labels i.e STK11,STK11-3UTR_1.
This was caused due to duplicate regions in Pan5117.bed, Pan3610.bed and Pan3608.bed
Naming of 6 GREM1_SCG5 region from Pan5117 also simplified.

## Add warning
Warning added to Logfile in earlier steps to avoid repeating similar error in future BED files.