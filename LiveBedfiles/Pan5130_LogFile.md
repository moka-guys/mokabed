# Pan4969 logfile
This BED file is used to calculate coverage for the TSO500 panel.
It consists of a subset of the 500+ genes on the panel, which are used for clinical reporting.
MANE select and MANEplusClinical transcripts for all genes have been selected.
Non coding regions from Pan4968 will be added.
This new version of the TSO500 coverage bedfile contains different genes from the previous bed file (Pan4969), some removed, others added, and therefore will replace the previous bed file.

## Transcript files
Two transcript files were generated based on the transcripts in the request form. The transcripts were identified using ensembl Biomart, providing the HGNC gene symbol and returning MANE and MANEplusClinical transcript lists
Files reformated with amended headers to match format required by mokabed. Accession added as 0 as will not be used by script anyway. The transcript files were checked by comparing the genes in the biomart output with the original list to ensure no genes were missed. Some of the gene symbols provided were out of date; the HGNC gene symbol was identified from the ensembl and HGNC websites and included in the list (TCEB1 is now ELOC and FAM123B is now AMER1). The files were also visually inspected to check for duplicates and errors. 

### transcript issues: SMARCA4
Taken from Pan5110_logfile.md:
    NM_001387283	SMARCA4	0	transcript not available in hg19
    one exon different between this transcript and the MANEselect NM_003072.
    exon 30
    | chr19        | Start    | Stop     |
    |--------------|----------|----------|
    | ensembl pos  | 11150133 | 11150229 |
    | 10bp padding | 11150123 | 11150239 |

Removed NM_001387283 from Pan5130_MANEplusClinicaltranscripts.txt
Take the missing exons from Pan5110 bed files to add manually later.

## Run mokabed
mokabed run in DNAnexus project 003_230602_Pan5130

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=003_230602_Pan5130:Pan5130_MANEtranscripts.txt -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=003_230602_Pan5130:Pan5130_MANEplusClinicaltranscripts.txt -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

### log files
see Pan5130_MANEtranscripts_LogFile.txt and Pan5130_MANEplusClinicaltranscripts_LogFile.txt for full details. Example command:
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5130_MANEplusClinicaltranscripts.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5130_MANEplusClinicaltranscriptsdata.bed --logfile /home/dnanexus/out/Output_files/Pan5130_MANEplusClinicaltranscripts_LogFile.txt`

## combining multiple transcripts
Run BEDtools subtract command to add regions from file a not already covered in file a to the end of file b:

`bedtools subtract -a 'Pan5130_MANEplusClinicaltranscriptsdata.bed' -b 'Pan5130_MANEtranscriptsdata.bed' >> Pan5130_MANEtranscriptsdata.bed`
`bedtools subtract -a 'Pan5130_MANEplusClinicaltranscriptsdataSambamba.bed' -b 'Pan5130_MANEtranscriptsdataSambamba.bed' >> Pan5130_MANEtranscriptsdataSambamba.bed`

Pan5130_MANEplusClinical BED files were deleted
`rm Pan5130_MANEplusClinicaltranscriptsdata*`

## Add intronic regions
concatenate intronic regions (Pan4968) into data.bed
`cat Pan4968.bed >> Pan5130_MANEtranscriptsdata.bed`

concatenate intronic regions (Pan4968) into dataSambamba.bed
`cat Pan4968.bed >> Pan5130_MANEtranscriptsdataSambamba.bed`

Manually modify Pan5130_MANEtranscriptsdata.bed and Pan5130_MANEplusClinicaltranscriptsdata.bed to match formatting (copied from Pan4969 bed files)

## sort bedfiles
### data.bed
`mv Pan5130_MANEtranscriptsdata.bed Pan5130_MANEtranscriptsdata_unsorted.bed; sort Pan5130_MANEtranscriptsdata_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan5130_MANEtranscriptsdata.bed; rm Pan5130_MANEtranscriptsdata_unsorted.bed`
header moved to top manually

### dataSambamba.bed
`mv Pan5130_MANEtranscriptsdataSambamba.bed Pan5130_MANEtranscriptsdataSambamba_unsorted.bed; sort Pan5130_MANEtranscriptsdataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan5130_MANEtranscriptsdataSambamba.bed; rm Pan5130_MANEtranscriptsdataSambamba_unsorted.bed`

## add chr
Added chr manually- shown to be required in previous testing for Pan4709

## rename
`mv Pan5130_MANEtranscriptsdata.bed Pan5130data.bed`
`mv Pan5130_MANEtranscriptsdataSambamba.bed Pan5130dataSambamba.bed`

## add extra SMARCA4 exon
copy line from Pan5110 bed files and re-sort

### data.bed
`mv Pan5130data.bed Pan5130data_unsorted.bed; sort Pan5130data_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan5130data.bed; rm Pan5130data_unsorted.bed`
header moved to top manually

### dataSambamba.bed
`mv Pan5130dataSambamba.bed Pan5130dataSambamba_unsorted.bed; sort Pan5130dataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan5130dataSambamba.bed; rm Pan5130dataSambamba_unsorted.bed`

## check all trasncripts included
Added full list of transcripts included.
`bash /home/rebecca/Documents/mokabed/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/transcript_checker.sh /home/rebecca/Documents/mokabed/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5130_all_transcripts.csv /home/rebecca/Documents/mokabed/mokabed/LiveBedfiles/Pan5130data.bed`
output:
`Bed file as expected (all transcripts present)`

## correct gene name in request form
KDM6A gene spelling error in request form. Had been corrected but not saved. Saved at this stage.

## testing
These bed files were tested using sambamba coverage and moka picard apps.

### Sambamba
The sambamba app was run on the HD200 sample from TSO23021 using the original dx run command, modified to use the correct BED file and output to the Pan5130 test project. 

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-G6vyyf00jy1kPkX9PJ1YkxB1 --detach -y --brief --name=TSO23021_01_230069_HD200_Pan5114.bam -ibam_index=project-GVk4zYj0FJGXXpjf8XGzpzfz:file-GVp8g1Q0zy03YKqGPxGXBFQ9 -ibamfile=project-GVk4zYj0FJGXXpjf8XGzpzfz:file-GVp8g1Q0zy043073qq0xbZqV -icoverage_level=100 -isambamba_bed=003_230602_Pan5130:/Pan5130dataSambamba.bed -imerge_overlapping_mate_reads=true -iexclude_failed_quality_control=true -iexclude_duplicate_reads=true -imin_base_qual=25 -imin_mapping_qual=30 --dest=003_230602_Pan5130`

app failed, last line of error: `AttributeError: gene id not in database: 11730`

11730 was the entrez id for TERT intronic regions, but it differs from the entrez id for the rest of TERT (newly added in Pan5130). 7130 is the GeneID in NCBI, 11730 is the HGNC id.
Manually changed all TERT regions to 7130 in both bed files and re-ran test. App completed successfully.

gene_level.txt report was checked and the correct number of genes was present.

### Picard
The MokaPicard app was previously found to fail with TSO500 bam files, presumed to be due to an issue with the bam. Therefore this bed file was tested with the NA12878 bam file from NGS536B (VCP3). App (v1.2) completed successfully suggesting the bed file is valid.

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-G9yJ57j0jy1ZV0fxPZZXJ8FJ --detach -y --brief --name=NGS536B_NA12878 -iCapture_panel=Hybridisation -isorted_bam=project-GPGYP2Q0PqFg20FY4J4Y51K3:file-GPGb0Fj00py9bGfq1jJ22zfv -ifasta_index=project-FVpfGp00vgV46F1xJx7y4YJ7:file-ByYgX700b80gf4ZY1GxvF3Jv -ivendor_exome_bedfile=Pan5130data.bed --dest=003_230602_Pan5130`
