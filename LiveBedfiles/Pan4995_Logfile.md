# Pan4995
This BED file describes the regions to be assessed (QC, coverage and variant filtering) for SNV variant calling on the VCP3 capture panel which has been updated In June 2022 to meet the changing test directory.

This BED file will be a modification to the existing VCP3 BED file, Pan4535. Pan4535 is the result of a few iterations and improvements from Pan4278 -> Pan4361 (corrected mapping of small exons in LAMA1,DIAPH1 and NBEA) and Pan4361 -> Pan4535 (addition of SNORD118 RNA).

This update includes a number of extra genes which have been added (see Pan4995_extras.txt) and a subset of genes that are already on the panel, but have some extra capture baits added to target promotor regions. These will be added with 5' UTRs padded by 10bp and only regions not already in Pan4535 will be incorporated (see Pan4995_extras_UTRs.txt)

## run mokabed for Pan4995_extras and Pan4995_extras_UTRs
`cat Pan4995_extras_LogFile.txt >> Pan4995_Logfile.md`
`cat Pan4995_extras_UTRs_LogFile.txt >> Pan4995_Logfile.md`

### Pan4995_extras mokabed
Time Stamp:2022-06-28 16:40:41.435955
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4995_extrasdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4995_extras.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4995_extrasdata.bed --logfile /home/dnanexus/out/Output_files/Pan4995_extras_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

### Pan4995_extras_UTRs mokabed
Time Stamp:2022-06-28 16:40:42.896945
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4995_extras_UTRsdataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --up 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4995_extras_UTRs.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4995_extras_UTRsdata.bed --logfile /home/dnanexus/out/Output_files/Pan4995_extras_UTRs_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## create copy of Pan4535data.bed
`cp Pan4535data.bed Pan4995data.bed`
## add Pan4995_extras to Pan4995data.bed
before adding Pan4995_extrasdata.bed to Pan4995data.bed the header was removed from Pan4995_extrasdata.bed (manually)
and a check was performed to look for shared regions 
`cut -f 1-4 Pan4995data.bed > Pan4995data_4col.bed; cut -f 1-4 Pan4995_extrasdata.bed > Pan4995_extras.data_4col.bed; bedtools intersect -a Pan4995data_4col.bed -b Pan4995_extras.data_4col.bed > Pan4995_extras_overlap.bed`
note Pan4995_extras_overlap.bed is empty denoting the new regions do not overlap any existing regions

remove these testing files
`git rm  Pan4995_extras_overlap.bed Pan4995_extras.data_4col.bed Pan4995data_4col.bed`
cat Pan4995_extrasdata.bed to Pan4995data.bed
`cat Pan4995_extrasdata.bed >> Pan4995data.bed`
## bedtools subtract to find regions in Pan4995_extras_UTRs not in Pan4995data.bed.
Find the regions in Pan4995_extras_UTRs with BEDtools subtract. However we first need to create 4 column BED files as bedtools errors if there are differing numbers of columns in a BED file.
`cut -f 1-4 Pan4995data.bed > Pan4995data_4col.bed; cut -f 1-4 Pan4995_extras_UTRsdata.bed > Pan4995_extras_UTRsdata_4col.bed; bedtools subtract -a Pan4995_extras_UTRsdata_4col.bed -b Pan4995data_4col.bed > Pan4995_extras_UTRs_extraregions.bed`
add these regions back to Pan4995data.bed
`cat Pan4995_extras_UTRs_extraregions.bed >> Pan4995data.bed `
Manually add in the rest of the row by searching for entrez gene id in rest of the file
## sort
`sort Pan4995data.bed -k1,1V -k2,2n -k3,3n > Pan4995_sorted.bed;mv Pan4995data.bed Pan4995_unsorted.bed; mv Pan4995_sorted.bed Pan4995data.bed; rm Pan4995_unsorted.bed`

## tidy up some testing files
`git rm Pan4995data_4col.bed Pan4995_extras_UTRsdata_4col.bed Pan4995_extras_UTRs_extraregions.bed`

## move header back to top in Pan4995data.bed
Done manually in vs code
## repeat for sambamba.bed - create copy of Pan4535dataSambamba.bed
`cp Pan4535dataSambamba.bed Pan4995dataSambamba.bed`
## add Pan4995_extras to Pan4995dataSambamba.bed
no need to repeat the test for overlapping regions as these regions are the same as in the data.bed file
`cat Pan4995_extrasdataSambamba.bed >> Pan4995dataSambamba.bed`
## bedtools subtract to find regions in Pan4995_extras_UTRs not in Pan4995dataSambamba.bed.
`bedtools subtract -a Pan4995_extras_UTRsdataSambamba.bed -b Pan4995dataSambamba.bed > Pan4995_extras_UTRsdataSambamba_subtracted.bed`
## add these regions to Pan4995dataSambamba.bed
`cat Pan4995_extras_UTRsdataSambamba_subtracted.bed >> Pan4995dataSambamba.bed`

## sort
`sort Pan4995dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4995sambamba_sorted.bed;mv Pan4995dataSambamba.bed Pan4995sambamba_unsorted.bed; mv Pan4995sambamba_sorted.bed Pan4995dataSambamba.bed; rm Pan4995sambamba_unsorted.bed`

## Testing
The app chanjo_sambamba_coverage_v1.13 and moka_picard_v1.1 were used to test these files using data from NGS487B_01_136819_NA12878_U_VCP3R81Via_Pan4146_S1 in 003_220628_Pan4995.
Both jobs completed without error.