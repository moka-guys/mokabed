# Pan3973
All data recieved from requester

As bioinformatics were involved in curating transcripts some usual steps for obtaining the transcripts (extracting from Moka) is non-standard
Pan3973 Pantranscripts list
The list of transcripts was created form a master list

## Pan3973_part1-4.txt
These files were manually curated, ensuring there were no duplicate transcripts for each gene. A check was also performed for duplicate transcripts.
## Pan3973_problem.txt
After running mokabed on Pan3973_part1.txt a problem was found with SMN1. This was removed from SMN1 to processing seperately later

## Pan3973_part1-4.txt
All 4 samples were run through mokabed. See each logfile for full logs but the commands executed have been extracted and saved below. 
```
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3973_part1.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3973_part1data.bed --logfile /home/dnanexus/out/Output_files/Pan3973_part1_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3973_part2.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3973_part2data.bed --logfile /home/dnanexus/out/Output_files/Pan3973_part2_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3973_part3.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3973_part3data.bed --logfile /home/dnanexus/out/Output_files/Pan3973_part3_LogFile.txt 
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan3973_part4.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan3973_part4data.bed --logfile /home/dnanexus/out/Output_files/Pan3973_part4_LogFile.txt 
```

## Combining multiple transcripts
Where multiple transcripts have been provided, the below BEDtools subtract command adds regions from file a not already covered in file b to the end of file b:

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part4data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part3data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part3data.bed'`

Adding regions from part4 to part3 does not include any additional regions.

Part4 BED files are deleted

### merging parts 2 and 3
Add regions from part 3 not included in part 2

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part3data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2data.bed'`
#### repeat for sambamba
`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part3dataSambamba.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2dataSambamba.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2dataSambamba.bed'`

Part3 BED files are deleted

### merging parts 1 and 2
Add regions from part 3 not included in part 2

`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2data.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1data.bed'`
#### repeat for sambamba
`bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part2dataSambamba.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1dataSambamba.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1dataSambamba.bed'`

Part2 BED files are deleted

## problematic transcript
Now all transcripts have been merged we need to add in NM_000344 (SMN1) which was causing mokabed to fail.
Mokabed was failing because cruzdb was returning multiple records for the same transcript.

The UCSC table browser was queried. selecting hg19, NCBI refseq track and the UCSC RefSeq (refGene) table, to match that used by MokaBED.

The identifier NM_000344 was provided and the output saved as Pan3973_problemRefSeqFormat.txt

### selection of transcript record
The two transcripts were assessed manually and it was found the one at chr5:69345495-69373422 was in the position of it's pseudogene SMN2 and should be ignored. This was confirmed with the requesting scientist, M Yau.

### creation of Pan3973_problemdata.bed
The following python code was used to create a BED file:
```
list1=[70220913,70234665,70237215,70238184,70238544,70240484,70241892,70247767,70248265]
list2=[70221011,70234737,70237335,70238385,70238697,70240580,70242003,70247821,70248842]
combined = zip(list1,list2)for i in combined:
    print "5\t" + str(i[0]) + "\t" + str(i[1])
```

NB. the list of coordinates were taken from the refseq format file


#### change to include cds
The cdsstart and cds end values were taken from the refseqformat bed file, essentially excluding any UTRs. This was checked with the USCS browser.

#### Add padding
The regions were padding +/-10bp as per those regions produced by MokaBED using the following python code:

```
with open('/home/aled/Documents/mokabed/LiveBedfiles Pan3973_problemdata.bed','r') as bedfile:
     for line in bedfile.readlines():
             chr,start,stop=line.split("\t")
             print str(chr)+"\t" + str(int(start)-10) + "\t" + str(int(stop)+10)
```

#### Add additional columns to Pan3973_problemdata.bed
Each line in the bed file contains 12 columns, We already have columns 1-3. Column4 contains the entrezgeneid and column 12 contains the genesymbol;transcript. All other columns are empty.

The rest of the line was manually created, based on an existing line from Pan3793_part1data.bed

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

#### Add regions to Pan3973_part1data.bed
The bedtools subtract command (below) was used to append SMN1 regions to the Pan3973_part1data.bed.

```
bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_problemdata.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1data.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1data.bed'
```

#### Create Pan3973_problemdataSambamba.bed
This BED file was generated using the existing mokabed function in the python shell (as per lines 1428-1431 of LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py):

```
from sambambaconvert import Sambamba
# Create sambamba file
sambamba = Sambamba()
sambamba.create_sambamba_bed(bedfile='/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_problemdata.bed', refseqfile='/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_problemRefSeqFormat.txt' , sambambaoutput='/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_problemdataSambamba.bed')
```

#### Add regions to Pan3973_part1dataSambamba.bed
```
bedtools subtract -a '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_problemdataSambamba.bed' -b '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1dataSambamba.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1dataSambamba.bed'
```


### Add extra BED files to Pan3973_part1data.bed
The following pre-defined BED files were requested to be added to this BED file Pan3604, Pan3607, Pan3612, Pan3621. Concatenate these to the end of the file.
```
cat '/home/aled/Documents/mokabed/LiveBedfiles/Pan3604.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan3607.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan3612.bed' '/home/aled/Documents/mokabed/LiveBedfiles/Pan3621.bed' >> '/home/aled/Documents/mokabed/LiveBedfiles/Pan3973_part1data.bed' 
```