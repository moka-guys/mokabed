Time Stamp:2020-12-16 09:47:48.936601
Command arguments executed:
RefSeq table format version generated as /home/dnanexus/out/Output_files/Pan4087dataRefSeqFormat.txt
/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4087.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4087data.bed --logfile /home/dnanexus/out/Output_files/Pan4087_LogFile.txt 

 Python version: 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

 getopt module file path: /home/dnanexus/anaconda2/lib/python2.7/getopt.py

 os module file path: /home/dnanexus/anaconda2/lib/python2.7/os.py

 pd class file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/pandas/__init__.py

 cruzdb module file path: /home/dnanexus/anaconda2/lib/python2.7/site-packages/cruzdb/__init__.py

version as defined by git tag = v1.2

## Manual addition of specified bases to Pan4087data.bed

The following region was added CHEK2 - This was to cover Chr22:29091857DelC - the only pertinent variant in this gene (others may be incidental findings)
22	29091856	29091857	11200										CHEK2;NM_007194.3

## Manual addition of specified bases to Pan4087dataSambamba.bed

The following region was added CHEK2 - This was to cover Chr22:29091857DelC - the only pertinent variant in this gene (others may be incidental findings)
22	29091856	29091857	22-29091856-29091857	0	+	CHEK2;NM_007194.3	11200

The data.bed and datasambamba.bed files have been tested using moka picard and chanjo coverage apps on DNA Nexus and completed without error.

## Further changes to chek2 base in Pan4087data.bed
After further tests using the BED to restrict variant calling we found we needed to add some padding to the chek2 variant.

The line

22	29091856	29091857	11200										CHEK2;NM_007194.3

was changed to

22	29091855	29091858	11200										CHEK2;NM_007194.3

## Further changes to chek2 base in Pan4087dataSambamba.bed
After further tests using the BED to restrict variant calling we found we needed to add some padding to the chek2 variant.

The line

22	29091856	29091857	22-29091856-29091857	0	+	CHEK2;NM_007194.3	11200

was changed to

22	29091855	29091858	22-29091855-29091858	0	+	CHEK2;NM_007194.3	11200

## Creation of a Congenica format csv file
### part 1 - selection of columns
To create a panel in congenica the following fields are required:

chr,start,stop,gene,transcript,autosomal_recessive,autosomal_dominant,x_linked,condition

The last 4 fields (autosomal_recessive,autosomal_dominant,x_linked,condition) are optional so will be set as 0 or left blank (condition)

Some bash commands were used to convert the data.bed into the required format:

```
# create a copy of the cvs template headers, named with the pan number
cp /home/aled/Documents/mokabed/LiveBedfiles/congenica_csv_template.csv /home/aled/Documents/mokabed/LiveBedfiles/Pan4087dataCongenica.csv
# take the chr, start, stop and gene;transcript columns from data.bed and convert to a csv
# split the line on semi colon to split the final field into 2 columns and concatenate onto the header
cut -f -3,14 /home/aled/Documents/mokabed/LiveBedfiles/Pan4087data.bed --output-delimiter=',' | cut -d ';' -f1,2 --output-delimiter=','  >> /home/aled/Documents/mokabed/LiveBedfiles/Pan4087dataCongenica_temp.csv
```

### part 2 - convert temp file into the csv template, with extra columns
```
# loop through temp file, ignore headers and adding four empty columns (denoted by 4 commas) to each row. write to the final csv file
while read line; do echo -e "${line},,,,"; done < <(grep -v "#" /home/aled/Documents/mokabed/LiveBedfiles/Pan4087dataCongenica_temp.csv) >> /home/aled/Documents/mokabed/LiveBedfiles/Pan4087dataCongenica.csv
# remove temp file
rm /home/aled/Documents/mokabed/LiveBedfiles/Pan4087dataCongenica_temp.csv
```