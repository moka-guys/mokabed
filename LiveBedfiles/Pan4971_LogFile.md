#Pan4971
This BEDfile will contain the SMN1 gene, padded +/-10bp, without the inclusion of any UTRs. It will also contain intronic regions described in Pan4972. This BED file will be used to calculate coverage for the LRPCR assay.

Unfortunately, the given transcript fails when run using MokaBED as two regions are returned. Following previous dicussions (see https://github.com/moka-guys/mokabed/blob/82cec9c9360c37d7bb1b03e7a3419ce974116fae/LiveBedfiles/Pan3973_log.md#selection-of-transcript-record) the desired regions were obtained from the UCSC table browser.

Following the instructions in the Pan3973_log.md a Python script was used to create Pan4971.bed
```
list1=[70220913,70234665,70237215,70238184,70238544,70240484,70241892,70247767,70248265]
list2=[70221011,70234737,70237335,70238385,70238697,70240580,70242003,70247821,70248842]
combined = zip(list1,list2)
for i in combined:
    print "5\t" + str(i[0]) + "\t" + str(i[1])
```