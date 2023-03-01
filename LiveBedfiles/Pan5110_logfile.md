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
exon 30
| chr19        | Start    | Stop     |
|--------------|----------|----------|
| ensembl pos  | 11150133 | 11150229 |
| 10bp padding | 11150123 | 11150239 |

Delete this transcript from Pan5110_transcripts2.txt and re-run mokabed

### logs
Both transcript files were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below.

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5110_transcripts1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5110_transcripts1data.bed --logfile /home/dnanexus/out/Output_files/Pan5110_transcripts1_LogFile.txt `

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5110_transcripts2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5110_transcripts2data.bed --logfile /home/dnanexus/out/Output_files/Pan5110_transcripts2_LogFile.txt `

## Identify transcripts for problem genes

### H3C14
Ensembl gene ENSG00000203811, coordinates from GRCh37 Chromosome 1: 149,811,110-149,812,765 reverse strand.
output from UCSC table browser:
```
#bin	name	chrom	strand	txStart	txEnd	cdsStart	cdsEnd	exonCount	exonStarts	exonEnds	score	name2	cdsStartStat	cdsEndStat	exonFrames
1727	NM_021059	chr1	-	149812258	149812780	149812318	149812729	1	149812258,	149812780,	0	H3C14	cmpl	cmpl	0,
1728	NM_021059	chr1	+	149824165	149824687	149824216	149824627	1	149824165,	149824687,	0	H3C14	cmpl	cmpl	0,
```
The ensembl coordinates overlap with bin 1727, so select this.
Gene has single exon, can be added manually:
| chr1         | Start     | Stop      |
|--------------|-----------|-----------|
| UCSC exon    | 149812318 | 149812729 |
| 10bp padding | 149812308 | 149812739 |
### H3C15
Ensembl gene ENSG00000203852, coordinates from GRCh37 Chromosome 1: 149,824,181-149,825,836 forward strand.
output from UCSC table browser:
```
#bin	name	chrom	strand	txStart	txEnd	cdsStart	cdsEnd	exonCount	exonStarts	exonEnds	score	name2	cdsStartStat	cdsEndStat	exonFrames
1727	NM_001005464	chr1	-	149812258	149812776	149812318	149812729	1	149812258,	149812776,	0	H3C15	cmpl	cmpl	0,
1728	NM_001005464	chr1	+	149824169	149824687	149824216	149824627	1	149824169,	149824687,	0	H3C15	cmpl	cmpl	0,
```
The ensembl coordinates overlap with bin 1728, so select this
Gene has single exon, can be added manually using cdsStart anf cdsStop:
| chr1         | Start     | Stop      |
|--------------|-----------|-----------|
| UCSC exon    | 149824216 | 149824627 |
| 10bp padding | 149824206 | 149824617 |

### CIC
Transcripts reviewed in ensembl and from UCSC table browser output
```
#bin	name	chrom	strand	txStart	txEnd	cdsStart	cdsEnd	exonCount	exonStarts	exonEnds	score	name2	cdsStartStat	cdsEndStat	exonFrames
911	NM_001304815	chr19	+	42772681	42799948	42775935	42799343	21	42772681,42775925,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797107,42797743,42798086,42798324,42798755,42798975,	42772746,42778729,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798456,42798887,42799948,	0	CIC	cmpl	cmpl	-1,0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
911	NM_001379480	chr19	+	42773403	42799948	42775935	42799343	21	42773403,42775925,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797110,42797743,42798086,42798324,42798755,42798975,	42773533,42778729,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798456,42798887,42799948,	0	CIC	cmpl	cmpl	-1,0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
911	NM_001379482	chr19	+	42773403	42799948	42775935	42799343	21	42773403,42775925,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797107,42797743,42798089,42798324,42798755,42798975,	42773533,42778729,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798456,42798887,42799948,	0	CIC	cmpl	cmpl	-1,0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
911	NM_001379484	chr19	+	42788620	42799948	42788856	42799343	20	42788620,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797107,42797743,42798086,42798324,42798755,42798975,	42788923,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798450,42798887,42799948,	0	CIC	cmpl	cmpl	0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
911	NM_001379485	chr19	+	42788620	42799948	42788856	42799343	20	42788620,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797107,42797743,42798089,42798324,42798755,42798975,	42788923,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798450,42798887,42799948,	0	CIC	cmpl	cmpl	0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
911	NM_015125	chr19	+	42788620	42799948	42788856	42799343	20	42788620,42790922,42791157,42791471,42791696,42791961,42793039,42793332,42793999,42794384,42795709,42796237,42796451,42796717,42797107,42797743,42798086,42798324,42798755,42798975,	42788923,42791072,42791392,42791601,42791879,42792127,42793242,42793558,42794103,42795618,42795897,42796359,42796618,42797011,42797433,42797988,42798241,42798456,42798887,42799948,	0	CIC	cmpl	cmpl	0,1,1,2,0,0,1,0,1,0,1,0,2,1,1,0,2,1,1,1,
```

3 transcripts selected to include in BED file which cover all regions:
NM_001304815
NM_001379482 
NM_015125

### RUNX1T1
Too many transcripts identified in ensembl and UCSC Table browser (15)
Illumina supplied TSO500 bed file contains:
NM_175636
NM_001198679
NM_004349
NM_001198628
NM_001198634
NM_001198633

## Make new transcript files
Pan5110_transcripts3-8 files created for the CIC and RUNX1T1 transcripts

## Run mokabed with transcript files 3-8
Run mokabed using same command as above, e.g.
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=003_230126_Pan5110:Pan5110_transcripts3.txt -icoding_up=10 -icoding_down=10 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false

### logs
See each logfile for full logs, example command executed has been extracted and saved below.

`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5110_transcripts3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5110_transcripts3data.bed --logfile /home/dnanexus/out/Output_files/Pan5110_transcripts3_LogFile.txt `

## combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

### parts 7 and 8
`bedtools subtract -a 'Pan5110_transcripts8data.bed' -b 'Pan5110_transcripts7data.bed' >> Pan5110_transcripts7data.bed`
`bedtools subtract -a 'Pan5110_transcripts8dataSambamba.bed' -b 'Pan5110_transcripts7dataSambamba.bed' >> Pan5110_transcripts7dataSambamba.bed`

part 8 files deleted `rm Pan5110_transcripts8data*`

### parts 6 and 7
`bedtools subtract -a 'Pan5110_transcripts7data.bed' -b 'Pan5110_transcripts6data.bed' >> Pan5110_transcripts6data.bed`
`bedtools subtract -a 'Pan5110_transcripts7dataSambamba.bed' -b 'Pan5110_transcripts6dataSambamba.bed' >> Pan5110_transcripts6dataSambamba.bed`

part 7 files deleted `rm Pan5110_transcripts7data*`

### parts 5 and 6
`bedtools subtract -a 'Pan5110_transcripts6data.bed' -b 'Pan5110_transcripts5data.bed' >> Pan5110_transcripts5data.bed`
`bedtools subtract -a 'Pan5110_transcripts6dataSambamba.bed' -b 'Pan5110_transcripts5dataSambamba.bed' >> Pan5110_transcripts5dataSambamba.bed`

part 6 files deleted `rm Pan5110_transcripts6data*`

### parts 4 and 5
`bedtools subtract -a 'Pan5110_transcripts5data.bed' -b 'Pan5110_transcripts4data.bed' >> Pan5110_transcripts4data.bed`
`bedtools subtract -a 'Pan5110_transcripts5dataSambamba.bed' -b 'Pan5110_transcripts4dataSambamba.bed' >> Pan5110_transcripts4dataSambamba.bed`

part 5 files deleted `rm Pan5110_transcripts5data*`

### parts 3 and 4
`bedtools subtract -a 'Pan5110_transcripts4data.bed' -b 'Pan5110_transcripts3data.bed' >> Pan5110_transcripts3data.bed`
`bedtools subtract -a 'Pan5110_transcripts4dataSambamba.bed' -b 'Pan5110_transcripts3dataSambamba.bed' >> Pan5110_transcripts3dataSambamba.bed`

part 4 files deleted `rm Pan5110_transcripts4data*`

### parts 2 and 3
`bedtools subtract -a 'Pan5110_transcripts3data.bed' -b 'Pan5110_transcripts2data.bed' >> Pan5110_transcripts2data.bed`
`bedtools subtract -a 'Pan5110_transcripts3dataSambamba.bed' -b 'Pan5110_transcripts2dataSambamba.bed' >> Pan5110_transcripts2dataSambamba.bed`

part 3 files deleted `rm Pan5110_transcripts3data*`

### parts 1 and 2
`bedtools subtract -a 'Pan5110_transcripts2data.bed' -b 'Pan5110_transcripts1data.bed' >> Pan5110_transcripts1data.bed`
`bedtools subtract -a 'Pan5110_transcripts2dataSambamba.bed' -b 'Pan5110_transcripts1dataSambamba.bed' >> Pan5110_transcripts1dataSambamba.bed`

part 2 files deleted `rm Pan5110_transcripts2data*`

## coding exons to be added manually
SMARCA4, H3C14 and H3C15 to be added manually as described above.

lines for data.bed
19	11150123	11150239	6597										SMARCA4;NM_001387283
1	149812308	149812739	126961										H3C14;NM_021059
1	149824206	149824617	333932										H3C15;NM_001005464

lines for dataSambamba.bed
19	11150123	11150239	19-11150123-11150239	0	+	SMARCA4;NM_001387283	6597
1	149812308	149812739	1-149812308-149812739	0	+	H3C14;NM_021059	126961
1	149824206	149824617	1-149824206-149824617	0	+	H3C15;NM_001005464	333932

Lines manually added to Pan5110_transcripts1data.bed and Pan5110_transcripts1dataSambamba.bed

## add intronic regions
concatenate intronic regions (Pan4968) into data.bed
`cat Pan4968.bed >> Pan5110_transcripts1data.bed`

concatenate intronic regions (Pan4968) into dataSambamba.bed
`cat Pan4968.bed >> Pan5110_transcripts1dataSambamba.bed`

