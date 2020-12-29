Time Stamp:2020-12-29 16:48:40.543158
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4098dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4098.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4098data.bed --logfile /home/dnanexus/out/Output_files/Pan4098_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

# Pan4098
This BED file contains genesrelevant to CMD, as described in the request file. Alist of transcripts is provided and two intronic variants.
As dicussed with the requesting scientists, 10bp of padding is applied.

This logfile is the output of mokabed and has been renamed as a markdown document.

## Manual addition of specified bases to Pan4098data.bed
The following intronic SNVs were added to Pan4098data.bed
21	47409880	47409881	1291										COL6A1;NM_001848.2
9	108368856	108368857	2218										FKTN;NM_001079802.2

## Manual addition of specified bases to Pan4098dataSambamba.bed
The following intronic SNVs were added to Pan4098dataSambamba.bed
21	47409880	47409881	21-47409880-47409881	0	+	COL6A1;NM_001848.2	1291
9	108368856	108368857	9-108368856-108368857	0	+	FKTN;NM_001079802.2	2218

### sort Pan4098data.bed
`sort Pan4098data.bed -k1,1V -k2,2n -k3,3n > Pan4098data_sorted.bed; mv Pan4098data.bed Pan4098data_unsorted.bed; mv Pan4098data_sorted.bed Pan4098data.bed; rm Pan4098data_unsorted.bed`

### move header back to top
done manually

### sort Pan4098dataSambamba.bed
`sort Pan4098dataSambamba.bed -k1,1V -k2,2n -k3,3n > Pan4098dataSambamba_sorted.bed; mv Pan4098dataSambamba.bed Pan4098dataSambamba_unsorted.bed; mv Pan4098dataSambamba_sorted.bed Pan4098dataSambamba.bed; rm Pan4098dataSambamba_unsorted.bed`
