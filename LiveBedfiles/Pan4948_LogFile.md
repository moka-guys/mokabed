# Pan4948

This BEDfile is a rename of Pan4310, the VCP2 +/-30bp panel, but this time with the whole of CHEK2 gene.

This panel consists of a number of genes which are to be padded +/-30 and one gene, PTEN which also requires the 5' UTR (also padded 30bp).
## Run MokaBED (This covers all genes except for PTEN - see Pan4948_PTEN_logfile.txt)
Time Stamp:2022-04-22 16:29:13.085148
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4948dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4948.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4948data.bed --logfile /home/dnanexus/out/Output_files/Pan4948_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Add PTEN
`cat Pan4948_PTENdata.bed >> Pan4948data.bed`
(header and sorting to follow)
remove header manually

## Add Pan4283
`cat Pan4283.bed >> Pan4948data.bed`

## remove duplicate chek2 region 
Pan4283 contains a region of chek2. The whole of chek2 is now included so this region does not need to be specified so it was removed manually.

## sort Pan4948data.bed
`sort Pan4948data.bed -k1,1V -k2,2n -k3,3n > Pan4948data_sorted.bed; mv Pan4948data.bed Pan4948data_unsorted.bed; mv Pan4948data_sorted.bed Pan4948data.bed; rm Pan4948data_unsorted.bed`
move header to the top manually

# make Pan4948_flat.bed
`cut -f1-3 Pan4948data.bed | bedtools merge > Pan4948_flat.bed`
Flat bed file used for somatic variant calling.

# make Pan4948dataSambamba.bed
## add pan4283 to sambamba.bed
`cat Pan4283.bed >> Pan4948dataSambamba.bed`

## manually modify intronic regions.
delete chek2 region and convert BRCA region into sambamba format

## add PTENsambamba.bed to pan4948sambamba.bed
`cat Pan4948_PTENdataSambamba.bed >> Pan4948dataSambamba.bed`

## sort sambambadata.bed
`sort Pan4948dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4948dataSambamba_sorted.bed; mv Pan4948dataSambamba.bed Pan4948dataSambamba_unsorted.bed; mv Pan4948dataSambamba_sorted.bed Pan4948dataSambamba.bed; rm Pan4948dataSambamba_unsorted.bed`

## delete intermediate/incomplete files
`rm Pan4948_PTENdata.bed Pan4948_PTENdataRefSeqFormat.txt Pan4948dataRefSeqFormat.txt Pan4948_PTENdataSambamba.bed`


## testing
Pan4948dataSambamba.bed was tested using sambamba_v1.13 - the app completed sucessfully
Pan4948data.bed was tested using filter_vcf_with_bedfile_v1.1 and moka_picard_v1.1 - both jobs completed sucessfully
Pan4948data_flat.bed was tested using varscan2_v1.7.1 and filter_vcf_with_bedfile_v1.1 - both jobs completed sucessfully

## fix data.bed+picard
Actually Picard did not complete properly with data.bed. 
an empty newline was removed from the bottom of the file.

Some additional testing was done incorrectly, as on the DNANexus UI some previous jobs were re-launched, but with the BED files replaced, however on closer inspection the jobs were not re-run with the newly made BED files.
testing was repeated

## testing
Pan4948dataSambamba.bed was tested using sambamba_v1.13 - the app completed sucessfully
Pan4948data.bed was tested using filter_vcf_with_bedfile_v1.1 and moka_picard_v1.1 - both jobs completed sucessfully
Pan4948data_flat.bed was tested using varscan2_v1.7.1 and filter_vcf_with_bedfile_v1.1 - both jobs completed sucessfully
