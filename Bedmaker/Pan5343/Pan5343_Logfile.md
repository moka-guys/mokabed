# Pan5343
CP205 CNV calling (R326) BED file (build37) for exomedepth CNV caller step.

## Save request form
Pan5343_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

No padding, no UTRs, and 2 additional regions specified to be included (ATM_3UTR, SMAD4_3UTR)

## Run refgene
Use Pan5343_transcript.txt to run refgene.py
```
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file ../../Bedmaker/Pan5343/Pan5343_transcript.txt --bed-format cnv --out Pan5343_CNV.bed
```

## Run bedmaker
Requested to add specified 3UTR regions to genes ATM and SMAD4. 
Saved outputs from BEDmaker.

## Add labels
Add labels to Pan5343_additional_regions_cnv.bed file

## Combine bedfiles
```
cat Pan5343_additional_regions_cnv.bed >> Pan5343_CNV.bed
```

## Sort bedfiles
Sort bedfile numerically
```
sort -k1,1V -k2,2n Pan5343_CNV.bed -o Pan5343_CNV.bed
```

## Mannually trim FOXC2 region
Edit FOXC2 regions to match Pan5346_exomeDepth.bed file.

## Testing
Pan5343_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.
