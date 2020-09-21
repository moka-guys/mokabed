# Pan3974
Bioinformaticians were involved in curating the list of transcripts for this gene panel, and at this point the transcripts were not available in Moka.
The list of transcripts is provided in LiveBedFiles/Pan3973 VCP3_Variant_v3.1.txt (Pan3973 is the variant BED file)
This was used to create LiveBedfiles/Transcripts/Pantranscriptfiles/Pan3973.txt - the format required by MokaBED and split into four seperate files (Pan3973_part1.txt,Pan3973_part2.txt etc )to ensure there are not duplicate transcripts for the same gene.
Copies of these files were created and named Pan3974

## problematic transcript
When creating Pan3973 it was found the SMN1 gene returns two records for the same transcripts which caused mokabed to fail. This transcript was excluded from this list and will be created manually.

## Run mokabed on Pan3973_part1-4.txt
These files were manually curated, ensuring there were no duplicate transcripts for each gene. A check was also performed for duplicate transcripts.

All 4 files were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below. 
```
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part1data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part1_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part2data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part2_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part3data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part3_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 50 --codingdown 50 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3974_part4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3974_part4data.bed --logfile /home/dnanexus/out/Output_files/Pan3974_part4_LogFile.txt 
```

## Combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part4data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed'`

Adding regions from part4 to part3 does not include any additional regions.

Part4 BED files are deleted

### merging parts 2 and 3
Add regions from part 3 not included in part 2

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2data.bed'`

#### repeat for parts 2 and 3 sambamba
`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part3dataSambamba.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2dataSambamba.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2dataSambamba.bed'`

Part3 BED files are deleted

### merging parts 1 and 2
Add regions from part 2 not included in part 1
`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part2data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1data.bed'`

### realised this BED file is for RPKM so sambamba bed file is not required - this won't be processed any further.
part 2 bedfiles removed

## problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which was causing mokabed to fail.
Mokabed was failing because cruzdb was returning multiple records for the same transcript.

The UCSC table browser was queried. selecting hg19, NCBI refseq track and the UCSC RefSeq (refGene) table, to match that used by MokaBED.

The identifier NM_000344 was provided and the output saved as Pan3974_problemRefSeqFormat.txt

### selection of transcript record
The two transcripts were assessed manually and it was found the one at chr5:69345495-69373422 was in the position of it's pseudogene SMN2 and should be ignored. This was confirmed with the requesting scientist, M Yau.

### creation of Pan3973_problemdata.bed
The following python code was used to create a BED file (using coordinates lists taken from the refseq format file)
```
list1=[70220913,70234665,70237215,70238184,70238544,70240484,70241892,70247767,70248265]
list2=[70221011,70234737,70237335,70238385,70238697,70240580,70242003,70247821,70248842]
combined = zip(list1,list2)
for i in combined:
    print "5\t" + str(i[0]) + "\t" + str(i[1])
```

#### change to include cds
The cdsstart and cds end values were taken from the refseqformat bed file, essentially excluding any UTRs. This was checked with the USCS browser.

#### Add padding
The regions were padding +/-50bp as per the regions produced by MokaBED using the following python code:

```
with open('/home/aled/Documents/mokabed/LiveBedfiles Pan3974_problem.bed','r') as bedfile:
     for line in bedfile.readlines():
             chr,start,stop=line.split("\t")
             print str(chr)+"\t" + str(int(start)-50) + "\t" + str(int(stop)+50)
```

#### Add additional columns to Pan3974_problem.bed
Each line in the bed file contains 12 columns, We already have columns 1-3. Column4 contains the entrezgeneid and column 12 contains the genesymbol;transcript. All other columns are empty.

The rest of the line was manually created, based on the data created when making Pan3973. The below has been copied from Pan3973_log.md

The entrez gene ID and accession version number was obtained using the existing mokabed function in the python shell as per lines 633 and 645 of LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py:
```
>>> from versionnumber_newtest import Liveaccversion, LiveRefLink
>>> liveacc = Liveaccversion()
>>> version = liveacc.versionfinder("NM_000344")
>>> print version
NM_000344.4
>>> liveref = LiveRefLink()
>>> entrez = liveref.entrezidretrieve("NM_000344")
>>> print entrez
6606
```

#### Add regions to Pan3974_part1data.bed
The bedtools subtract command (below) was used to append SMN1 regions to the Pan3974_part1data.bed.

```
bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_problem.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1data.bed'
```

### sort Pan3974_part1data.bed
sort the bed file.
```
sort Pan3974_part1data.bed -k1,1V -k2,2n -k3,3n > Pan3974_part1data_sorted.bed; mv Pan3974_part1data.bed Pan3974_part1data_unsorted.bed; mv Pan3974_part1data_sorted.bed Pan3974_part1data.bed; rm Pan3974_part1data_unsorted.bed
```

The header was moved back to the top manually

### make the RPKM bedfile
Pan3974_part1data.bed was converted to the RPKM BEDfile format by running the RPKM_bedfile DNANexus app (v1.0) in project 003_200918_Pan3974_bedfile.
Pan3608 was added in. 
Logfiles and output saved to repo

### rename 
rename the RPKM BED file
```
mv '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1_RPKM.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_RPKM.bed' 
mv '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_part1_RPKM_logfile.txt' '/home/aled/Documents/mokabed/LiveBedfiles/Pan3974_RPKM_logfile.txt' 
```

### test
The BED file was tested using RPKM_using_conifer_v1.6 which ran without error