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

    