# This bed file is the capture BED file for TWIST EXOME kit.
## Two files were provided by TWIST:
Twist_Exome_RefSeq_targets_hg19.bed - contains the kit with added refseq baits
Twist_Exome_Target_hg19.bed - contains the CCDS only

BEDtools intersect command (below) showed there were regions in the CCDS bedfile, not in the refseq bedfile.
`bedtools intersect -v -a 'Twist_Exome_Target_hg19.bed' -b 'Twist_Exome_RefSeq_targets_hg19.bed`

Therefore the BED files should be combined, sorted and merged:
cat Twist_Exome_RefSeq_targets_hg19.bed >> 'Twist_Exome_Target_hg19.bed'

## sort
`sort -k1,1 -k2,2n Twist_Exome_Target_hg19.bed > Twist_Exome_RefSeq_targets_hg19_sorted.bed`

## merge
`bedtools merge -i Twist_Exome_RefSeq_targets_hg19_sorted.bed > Twist_Exome_RefSeq_targets_hg19_sorted_merged.bed`

## rename (and remove all temp files)
`git mv Twist_Exome_RefSeq_targets_hg19_sorted_merged.bed Pan2385.bed`

## remove chr
`sed -i 's/chr//' Pan2385.bed`

## rename to reflect the kit design
`git mv Pan2385.bed Twist_Exome_RefSeq_CCDS_v1.2.bed`
`git mv Pan2385.LogFile.txt Twist_Exome_RefSeq_CCDS_v1.2_LogFile.txt`

## create padded.bed
using the below code create a padded code:

```
# list to hold modified bedfile
list = []
# open unpadded bed
with open('/home/aled/mokabed/LiveBedfiles/Twist_Exome_RefSeq_CCDS_v1.2.bed','r') as bed:
    # for each line capture the three columns
    for line in bed:
        chr,start,stop = line.split("\t")
        # pad by 100 bases and tab delimited string to list
        list.append(chr+"\t"+str(int(start)-100)+"\t"+str(int(stop)+100)+"\n")
# create padded bedfile and write list to file.
with open('/home/aled/mokabed/LiveBedfiles/Twist_Exome_RefSeq_CCDS_v1.2_padded.bed','w') as newbed:
    newbed.writelines(list)
```

## repeat merge step on padded bed
`bedtools merge -i Twist_Exome_RefSeq_CCDS_v1.2_padded.bed > Twist_Exome_RefSeq_CCDS_v1.2_padded_merged.bed`

## rename merged padded bed
`git rm Twist_Exome_RefSeq_CCDS_v1.2_padded.bed`
`git mv Twist_Exome_RefSeq_CCDS_v1.2_padded_merged.bed Twist_Exome_RefSeq_CCDS_v1.2_padded.bed`

## rename unpadded bed (targets bedfile)
`git mv Twist_Exome_RefSeq_CCDS_v1.2.bed Twist_Exome_RefSeq_CCDS_v1.2_targets.bed`
