Time Stamp:2020-12-15 17:22:23.048958
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4086dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 10 --codingdown 10 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4086.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4086data.bed --logfile /home/dnanexus/out/Output_files/Pan4086_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2


## Manual addition of specified bases to Pan4086data.bed


Two further regions were added:

CHEK2 - This was to cover Chr22:29091857DelC

22	29091856	29091857	11200										CHEK2;NM_007194.3

An SNV at -11bp was also added in by changing an existing row:
17	41256874	41256983	672										BRCA1;NM_007294.4

Was changed to:

17	41256874	41256984	672										BRCA1;NM_007294.4


## Manual addition of specified bases to Pan4086dataSambamba.bed

Two further regions were added:

CHEK2 - This was to cover Chr22:29091857DelC

22	29091856	29091857	22-29091856-29091857	0	+	CHEK2;NM_007194.3	11200

An SNV at -11bp was also added in by changing an existing row:

17	41256874	41256983	17-41256874-41256983	0	+	BRCA1;NM_007294.4	672

Was changed to:

17	41256874	41256984	17-41256874-41256984	0	+	BRCA1;NM_007294.4	672

The data.bed and datasambamba.bed files have been tested using moka picard and chanjo coverage apps on DNA Nexus and completed without error.

## Further modifications to chek2 base in Pan4086data.bed

Further testing of using the data.bed file to restrict variant calling showed the chek2 variant needing padding.

The line 

22	29091856	29091857	11200										CHEK2;NM_007194.3

was changed to

22	29091855	29091858	11200										CHEK2;NM_007194.3

## Further modifications to chek2 base in Pan4086dataSambamba.bed

Further testing of using the data.bed file to restrict variant calling showed the chek2 variant needing padding.

The line 

22	29091856	29091857	22-29091856-29091857	0	+	CHEK2;NM_007194.3	11200

was changed to

22	29091855	29091858	22-29091855-29091858	0	+	CHEK2;NM_007194.3	11200

## Creation of a Congenica format csv file

To create a panel in congenica the following fields are required:

chr,start,stop,gene,transcript,autosomal_recessive,autosomal_dominant,x_linked,condition

The last 4 fields (autosomal_recessive,autosomal_dominant,x_linked,condition) are optional so will be set as 0 or left blank (condition)

Some bash commands were used to convert the data.bed into the required format:

```
cp /home/aled/Documents/mokabed/LiveBedfiles/congenica_csv_template.csv /home/aled/Documents/mokabed/LiveBedfiles/Pan4086dataCongenica.csv; cut -f -3,14 /home/aled/Documents/mokabed/LiveBedfiles/Pan4086data.bed --output-delimiter=',' | cut -d ';' -f1,2 --output-delimiter=','  >> /home/aled/Documents/mokabed/LiveBedfiles/Pan4086dataCongenica_temp.csv
while read line; do echo -e "${line},,,,"; done < <(grep -v "#" /home/aled/Documents/mokabed/LiveBedfiles/Pan4086dataCongenica_temp.csv) >> /home/aled/Documents/mokabed/LiveBedfiles/Pan4086dataCongenica.csv
rm /home/aled/Documents/mokabed/LiveBedfiles/Pan4086dataCongenica_temp.csv
```