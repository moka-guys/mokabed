# Pan5110 logfile
This BED file contains the coding regions (+/-10bp) for all 523 genes included in the TSO500 capture. It has been made to allow coverage reports to be generated for all genes, sometimes required for adhoc requests from clinicians to analyse genes not included in national genomic test directory panels.
The TSO500 gene list was checked to ensure gene symbols are up to date using the Ensembl biomart tool. 32 genes had out of date gene symbols. The BED file request form includes the gene name on the Illumina list and the HGNC gene symbol.
Transcript selection used MANE select and MANE plus clinical transcripts for most (521 genes). Two remaining genes to be added separately, RUNX1T1 and TERC. 
TERT promoter regions are also included, taken from Pan4968.

## Transcript and gene list files
Two transcript list files created (transcripts 2 contains second transcripts for 10 genes, mostly MANE plus clinical).
A gene list for, Pan5110_genelist.txt created to use running mokabed with gene symbols for RUNX1T1 because a specific transcript could not be identified.

The transcript lists were created using the original list from Illumina, and using ensembl biomart to check gene symbols and identify MANE transcripts. Total number of genes = 523 at all stages.

## Run mokabed
mokabed run in DNAnexus project 003_230126_Pan5110

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=003_230126_Pan5110:Pan5110_transcripts1.txt -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=003_230126_Pan5110:Pan5110_transcripts2.txt -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

### transcript issues
dnanexus_mokabed failed. Investigation identified the issues below. In order to check what transcripts were available in UCSC the [UCSC table browser](https://genome-euro.ucsc.edu/cgi-bin/hgTables) was queried. selecting hg19, NCBI refseq track and the UCSC RefSeq (refGene) table, to match that used by MokaBED.

#### Pan5110_transcripts1.txt
NM_001386298	CIC	0	transcript not available in hg19
transcripts compared and no obvious equivalent for this transcript available in UCSC hg19
NM_021059	H3C14	0	2 entries for same transcript in UCSC
NM_001005464	H3C15	0	2 entries for same transcript in UCSC
Add these genes to Pan5110_genelist.txt

Delete these transcripts from Pan5110_transcripts1.txt and re-run mokabed

#### Pan5110_transcripts2.txt
NM_001387283	SMARCA4	0	transcript not available in hg19
one exon different between this transcript and the MANEselect NM_003072. Add this exon manually later.
Delete this transcript from Pan5110_transcripts2.txt and re-run mokabed

### logs
Both transcript files were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below.

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5110_transcripts1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5110_transcripts1data.bed --logfile /home/dnanexus/out/Output_files/Pan5110_transcripts1_LogFile.txt `

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5110_transcripts2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5110_transcripts2data.bed --logfile /home/dnanexus/out/Output_files/Pan5110_transcripts2_LogFile.txt `