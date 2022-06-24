# Pan4973
This BED file is used to do read count step of exome depth for CNV analysis of VCP2.
This BED file has been previously made in Pan4301 and Pan4771. This BED file includes the entirety of CHEK2, not just the intronic region listed in Pan4283 (rs555607708). This will also have the CNV control sites added (Pan3608).

# run mokabed
Time Stamp:2022-06-24 13:30:35.761741
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4973dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4973.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4973data.bed --logfile /home/dnanexus/out/Output_files/Pan4973_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2


## Combine PTEN bed files
`cat Pan4973_PTENdata.bed >> Pan4973data.bed`
remove header
## add Pan4283, Pan3610 and Pan3608
`cat Pan4283.bed >> Pan4973data.bed`
remove the chek2 variant from Pan4283 that overlaps with chek2 variant
`cat Pan3608.bed >> Pan4973data.bed`
`cat Pan3610.bed >> Pan4973data.bed`
## generate intermediary BED4 file for capture regions
Need to make a 4 column bed file, where the 4th column:
1) contains no underscores - replace any underscores with dashes.
2) contains the gene symbols, not entrezgene ids.

first, in excel split the 12th column on semi colon and then replace entrez gene id with gene symbols
`mv Pan4973data.bed Pan4973data_12col.bed; cut -f1-4 Pan4973data_12col.bed > Pan4973data.bed; rm Pan4973data_12col.bed`

next, in vscode, replace underscores and quotation marks (produced by spreadsheet software)
## generate intermediary exomedepth files for exons
`TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan4973 Pan4973data.bed`

## set sorted list of missed (non-exonic) capture regions
`mv _Pan4973_missed.bed _Pan4973_missed_unsorted.bed; sort -k1n,1 -k2n,3n _Pan4973_missed_unsorted.bed > _Pan4973_missed.bed; rm Pan4973_missed_unsorted.bed`
repeat but statuing chr column is numeric
## amend missed (non-exonic) regions with:
### 1. strand information (BED6)
Performed in vscode.
5th column was set to 0
6th column was set to + or -.
This was taken from _Pan4771_extra.bed.
All CNVs from Pan3608 were given as + strand but this shouldn't have any effect as they will not be grouped.
## regenerate (final) exomedepth files giving the additional non-exonic regions from last step
`TestArea_for_bed_generation_script/makeExomedepth.sh hg19 _Pan4973 Pan4973data.bed _Pan4973_missed.bed`
note after this stage there are no missed regions (_missed.bed is empty)

## set sorted list of missed (non-exonic) capture regions
`mv _Pan4973_exomedepth.bed _Pan4973_exomedepth_unsorted.bed; sort -k1n,1 -k2n,3n _Pan4973_exomedepth_unsorted.bed > _Pan4973_exomedepth.bed; rm _Pan4973_exomedepth_unsorted.bed`

## rename exome depth
`git mv _Pan4973_exomedepth.bed Pan4973_exomedepth.bed`