# Pan5211
This VCP3 BED file is a remake of Pan5192, few requested genes(DOLK,FANCF,NHLRC1,PRKACG,RNF113A,THBD,RNU4ATAC) were found to be missing from Pan5192.

From past attempts of making this BED file there are additional steps required to create this BED file: -
 - SNORD118 and RNU4ATAC genes are non-coding RNA, so don't have a NM number. Therefore must be added manually. 
 - LAMA2,DIAPH1,NBEA mapped incorrectly in the UCSC refseq database. This needs to be corrected. 
 - SMN1 was found to be problematic therefore has to be done manually.
 - Note MTTP transcript had to be changed from NM_001386140 to NM_000253 as mokabed couldn't find the transcript in the database.   Both transcripts were compared and no differences were found.

 # Create Transcript files
For few genes multiple transcript have been requested, these were separated into Pan5211.txt, Pan5211_part1.txt, and Pan5211_part2.txt

# Run Mokabed
Time Stamp:2024-02-28 11:58:14.098253
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan5211dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 0 --codingdown 0 --up 0 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan5211.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan5211data.bed --logfile /home/dnanexus/out/Output_files/Pan5211_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Combine multiple transcripts
merge Pan5211_part1data.bed and Pan5211_part2data.bed

bedtools subtract -a Pan5211_part2data.bed -b Pan5211_part1data.bed  >> Pan5211_part1data.bed

merge Pan5211_part1data.bed with Pan5211data.bed 

bedtools subtract -a Pan5211_part1data.bed -b Pan5211data.bed >> Pan5211data.bed