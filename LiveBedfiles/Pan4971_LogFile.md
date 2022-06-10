# Pan4971
This BEDfile will contain the SMN1 gene, padded +/-10bp, without the inclusion of any UTRs. It will also contain intronic regions described in Pan4972. This BED file will be used to calculate coverage for the LRPCR assay.

Unfortunately, the given transcript fails when run using MokaBED as two regions are returned. Following previous dicussions (see https://github.com/moka-guys/mokabed/blob/82cec9c9360c37d7bb1b03e7a3419ce974116fae/LiveBedfiles/Pan3973_log.md#selection-of-transcript-record) the desired regions were obtained from the UCSC table browser.

### Create Pan4971.bed
Following the instructions in the Pan3973_log.md a Python script was used to create Pan4971.bed
```
list1=[70220913,70234665,70237215,70238184,70238544,70240484,70241892,70247767,70248265]
list2=[70221011,70234737,70237335,70238385,70238697,70240580,70242003,70247821,70248842]
combined = zip(list1,list2)
for i in combined:
    print "5\t" + str(i[0]) + "\t" + str(i[1])
```

### Add additional columns to Pan4971.bed
Each line in the bed file contains 12 columns, We already have columns 1-3. Column4 contains the entrezgeneid and column 12 contains the genesymbol;transcript. All other columns are empty.

The rest of the line was manually created, based on an existing line from another data.bed

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

### Add padding
The regions were padding +/-10bp as per those regions produced by MokaBED using the following python code:

```
with open('/home/aled/Documents/201229_mokabed/mokabed/LiveBedfiles/Pan4971.bed','r') as bedfile:
    for line in bedfile.readlines():
            chr,start,stop=line.split("\t")[0:3]
            print str(chr)+"\t" + str(int(start)-10) + "\t" + str(int(stop)+10)+\t"+"\t".join(line.rstrip().split("\t")[3:])
```

### Create sambamba file
This file was taken from the git history from Pan3973 - see https://github.com/moka-guys/mokabed/blob/8a4899668e82b6dd201f50a3c58e15b302164e9a/LiveBedfiles/Pan3973_problemdataSambamba.bed
This file was saved as Pan4971dataSambamba.bed


### Add Pan4972
Add intronic regions
`cat Pan4972.bed >> Pan4971.bed`
`cat Pan4972.bed >> Pan4971dataSambamba.bed` 

### format intronic regions in bedfile
This was done manually. In Pan4971.bed it was copied from the line above, but preserving the RSID in place of the entrezgeneid. It's unlikely these columns are used for grouping - this is more relevant for the sambamba.bed.

For the sambamba bedfile the rsid was used inplace of the transcript. The entrezgeneid is used to group lines in the BEDfile into gene level coverage.

### sort Pan4971data.bed
`mv Pan4971.bed Pan4971data_unsorted.bed; sort Pan4971data_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4971.bed; rm Pan4971data_unsorted.bed`

### rename to data.bed
`git mv Pan4971.bed Pan4971data.bed`

### sort Pan4971dataSambamba.bed
`mv Pan4971dataSambamba.bed Pan4971dataSambamba_unsorted.bed; sort Pan4971dataSambamba_unsorted.bed -k1,1V -k2,2n -k3,3n > Pan4971dataSambamba.bed; rm Pan4971dataSambamba_unsorted.bed`