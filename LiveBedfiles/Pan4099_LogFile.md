Time Stamp:2020-12-29 15:40:33.289397
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4099dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4099.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4099data.bed --logfile /home/dnanexus/out/Output_files/Pan4099_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Pan4099
This BED file contains 4 genes. One of which (LDLR) requires the 5' UTR and another (APOB) only requires a specified exon.
As dicussed with the requesting scientists 10bp of padding is required.

Mokabed was run twice. Once for LDLR, including the 5' UTR (Pan4099_LDLR*) and another with the remaining genes (excluding LDLR and APOB). 

### concatenating Pan4099*data.bed
`cat Pan4099_LDLRdata.bed >> Pan4099data.bed; rm Pan4099_LDLRdata.bed`

### concatenating Pan4099*dataSambamba.bed
`cat Pan4099_LDLRdataSambamba.bed >> Pan4099dataSambamba.bed; rm Pan4099_LDLRdataSambamba.bed`

### delete refseq files
As these are not used and will not be modified these are deleted - these can be retrieved from version control if required.

### remove duplicate header from Pan4099data.bed
This was done manually.

### Add APOB region to Pan4099data.bed
The following line was added to Pan4099data.bed
2	21227941	21235533	338										APOB;NM_000384

### Add APOB region to Pan4099dataSambamba.bed
The following line was added to Pan4099dataSambamba.bed
2	21227941	21235533	2-21227941-21235533	0	+	APOB;NM_000384	338

### sort Pan4099data.bed
`sort Pan4099data.bed -k1,1V -k2,2n -k3,3n > Pan4099data_sorted.bed; mv Pan4099data.bed Pan4099data_unsorted.bed; mv Pan4099data_sorted.bed Pan4099data.bed; rm Pan4099data_unsorted.bed`

### move header back to top
done manually

### sort Pan4099dataSambamba.bed
`sort Pan4099dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4099dataSambamba_sorted.bed; mv Pan4099dataSambamba.bed Pan4099dataSambamba_unsorted.bed; mv Pan4099dataSambamba_sorted.bed Pan4099dataSambamba.bed; rm Pan4099dataSambamba_unsorted.bed`

### testing statement
Pan4099dataSambamba.bed and Pan4099data.bed were tested using Moka_picard_v1.1 and coverage_using_sambamba_and_chanjo_v1.10 in 003_201229_Pan4099.
Both jobs completed without error.