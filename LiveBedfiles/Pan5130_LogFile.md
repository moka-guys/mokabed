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