# Pan5217

This is a remake of the VCP3 exomedepth readcount BEDfile.

During the validation of Pan5211_exomedepth.bed(https://github.com/moka-guys/mokabed/blob/master/LiveBedfiles/Pan5211_exomedepth.bed) it was noticed CARS1 gene was missing.

The process of generating a VCP3 Exomedepth readcount bedfile is very complicated, the quickest solution to this problem without restarting from scratch, was to create the CARS1 bedfile seperately and join the output with Pan5211 creating Pan5217_exomedepth.bed

## Save CARS1 transcript file

## Run Mokabed for CARS1
Time Stamp:2024-03-15 09:49:19.826707
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/cars_transcriptdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/cars_transcript.txt --minuschr --outputfile /home/dnanexus/out/Output_files/cars_transcriptdata.bed --logfile /home/dnanexus/out/Output_files/cars_transcript_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

#############
Create CARS1 exomedepth bedile
#############

## Replace Entrez ID with gene symbols

a) Open cars_transcriptdata.bed in Excel, first split the GeneAccession column on semi colon and create a column concatenating EntrezID;GeneSymbol. Excel saves file as a csv, so open file in VS code and replace "," with a tab. This helps visualise changes during code review

b) In Excel format Entrez;Gene_Accession to only include gene symbol. Use find and replace to edit Entrez;Gene_Accession column to only include Gene symbols. Find *; and and leave replace field empty (remember to select wildcard option) Excel saves output as csv, in VScode replace "," with a tab

c) Delete Entrez ID column

## Convert 4 column format
cut -f1-4 cars_transcriptdata.bed > cars_transcriptdata_4col.bed

## Run makeExomedepth.sh
Generate intermediary exomedepth files for exons:
    TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _CARS1 cars_transcriptdata_4col.bed

## Rename exomedepth file
git mv _CARS1_exomedepth.bed CARS1_exomedepth.bed

## Delete unrequired files
rm _CARS*

## copy Pan5211_exomedepth.bed

cp Pan5211_exomedepth.bed Pan5217_exomedepth.bed

## combine CARS1_exomedepth.bed

cat CARS1_exomedepth.bed >> Pan5217_exomedepth.bed

## Sort and rename
sort Pan5217_exomedepth.bed -k1,1V -k2,2n -k3,3n > Pan5217_exomedepth_sorted.bed; mv Pan5217_exomedepth.bed Pan5217_exomedepth.bed_unsorted.bed; mv Pan5217_exomedepth_sorted.bed Pan5217_exomedepth.bed; rm Pan5217_exomedepth.bed_unsorted.bed

## Gene list check
Check all genes in the bedfile request form are present in the final bedfile.

- Save Pan5217 request form (This was approved by Michael Yau)

1. Take a copy of Pan5211_exomedepth.bed 
    cp Pan5217_exomedepth.bed Pan5217_genecheck.csv

2. Open Pan5217_genecheck.csv use "_" to seperate gene name from exon number and delete the exon number column

3. Add header: Chr,Start,Stop,Gene

4. Create all transcript file; copy the genes and transcript list in the request form into an empty Excel file and save it as a CSV file

5. Run compare_genelists.py

python3 ~/Documents/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py Pan5217_genecheck.csv /home/natasha/Documents/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5217_alltranscripts.csv Gene Gene

Output: 
Genes missing:
{'HYCC1', 'GBA1', 'MTRFR'}

Troubleshooting
hycc1= FAM126A 
mtrfr = C12orf65
GBA1= GBA 

Script was run a second time to check addiotional genes present in data.bed which weren't requested

python3 ~/Documents/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/compare_genelists.py /home/natasha/Documents/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5217_alltranscripts.csv Pan5217_genecheck.csv Gene Gene

Genes missing:
{'CNV08', 'FAM126A', 'BRCA1-IN11-1', 'CNV12-1', 'CNV11', 'RNU4ATAC', 'CNV09-1', 'CNV16-1', 'BRCA1-PM-5-2', 'CNV13', 'CNV10-1', 'C12orf65', 'BRCA1-IN12-1', 'CNV02-1', 'BRCA1-IN11-2', 'CNV07', 'CNV15', 'BRCA1-PM-5-1', 'CNV03', 'BRCA1-PM-5-3', 'GBA', 'BRCA1-PM-5-4', 'CNV14-1', 'BRCA1-IN12-2'}

Regions highlighted are the additionally requested regions e.g CNV control sites, intronic regions
RNU4ATAC is an RNA gene not included in the request form but MYau confirmed the gene is required.

## Update request form

Add RNU4ATAC to the request form

## Bedtools substract

It was noticed makeExomedepth.sh script struggles with single coding exon genes, leading to omission of coding regions mapping in the bedfiles.
The lack of presense of these regions in the readcount bedfile led to these genes being excluded from analysis and omission in the header of the exomedepth report. The CNV calling bedfiles are not created using makeexomedepth.sh therefore, these bedfiles are correctly made. 

Bedtools subtract was used to identify unique regions present in the CNV calling bedfile that are not present in the readcount bedfile. Any missing regions highlighted will be manually included in this BEDfile.

VCP3 has 7 tests that require CNV analysis: R79 R81 R66 R229 R227 R90 R97 

bcftools subtract was performed to find unique regions in the CNV calling BED files for each of these regions

**R79**
bedtools subtract -a Pan5168_CNV.bed -b Pan5217_exomedepth.bed -A
3	43121150	43122953	84892 POMGNT2 
This has highlighed POMGNT2 exon 2 was excluded from Pan5217_exomedepth.bed. Pan5168_CNV.bed (https://github.com/moka-guys/mokabed/blob/master/LiveBedfiles/Pan5168_LogFile.md) was padded by +/-30bp, therefore padding will be removed from the exon2 region above to keep it consistent with the padding in other regions in Pan5217_exomedepth.bed

Manual correcttion to Pan5217_exomedepth.bed
3   43121180    43122923    POMGNT2_1 (reverse strand)


6	129763336	129763402	3908    LAMA2
This region was also highlighted as missing from Pan5217_exomedepth.bed

Previously, it was noted that mokabed mapped LAMA2 exon 44 incorrectly, and so it was manually corrected in Pan5211_exomedepth.bed. The coordinates were verfied in UCSC using NM_000426 refseq transcript. The LAMA2 incorrectly mapped exon44 was not corrected in Pan5168_CNV.bed which is why the difference is being observed.

**R90**
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5171_CNV.bed -A
3	151055574	151056663	64805 P2RY12

Exon 3 of P2RY12 was not included by makeExomedepth.sh, Pan5171_CNV.bed (https://github.com/moka-guys/mokabed/blob/master/LiveBedfiles/Pan5171_LogFile.md) was padded by +/-30bp, therefore padding will be removed from the exon3 region above to keep it consistent with the padding in other regions in Pan5217_exomedepth.bed

Manual correcttion to Pan5217_exomedepth.bed:
3   151055604   151056633   P2RY12_3

5	140915590	140915659	1729 DIAPH1
This region was also highlighted as missing from Pan5217_exomedepth.bed

Previously, it was noted that mokabed mapped DIAPH1 exon 18 incorrectly, and so it was manually corrected in Pan5211_exomedepth.bed. The coordinates were verfied in UCSC using NM_005219 refseq transcript. The DIAPH1 incorrectly mapped exon18 was not corrected in Pan5168_CNV.bed which is why the difference is being observed.

19	3594803	3595104	6915    TBXA2R
Difference is due to different transcripts used to make Pan5171_CNV.bed (NM_201636) and Pan5211_exomedepth.bed (NM_001060)

Michael Yau and Mike Mitchel confirmed NM_001060 is the preferred transcript, therefore no changes are required to Pan5217_exomedepth.bed

**R81** 
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5170_CNV.bed -A
No unique regions in CNV BED file

**R66**
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5174_CNV.bed -A
No unique regions in CNV BED file

**R229**
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5179_CNV.bed -A
No unique regions in CNV BED file

**R227**
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5177_CNV.bed -A
No unique regions in CNV BED file

**R97** 
bedtools subtract -b Pan5217_exomedepth.bed -a Pan5173_CNV.bed -A
No unique regions in CNV BED file

CNV analysis not required for:R56, R57, R58, R60, R62 
