# Pan5331
CP205 CNV calling (R97) BED file (build37) for exomedepth CNV caller step.

## Save request form
Pan5331_request_form.csv was used (added into mokabed/LiveBedfiles/RequestForms)

No padding and no UTRs to be included. Two transcripts have been specified for use to cover gene ADAMTS13 (NM_139027.6,NM_139025.5).

## run refgene
Use Pan5331_transcript.txt to run refgene.py
```
python3 refgene.py --refgene ncbiRefSeq.txt --transcript-file ../../Bedmaker/Pan5331/Pan5331_transcript.txt --bed-format cnv --out Pan5331_CNV.bed
```

## Sort Pan5331_CNV.bed
Sort Pan5331_CNV.bed numerically
```
sort -k1,1V -k2,2n Pan5331_CNV.bed -o Pan5331_CNV.bed
```

## Trim THBD region
Mannually trim the THBD BED region in Pan5331_CNV.bed to match Pan5346_exomeDepth.bed (to fix the previous single exon gene issue).

## Testing
Pan5331_CNV.bed was tested in DNAnexus using ED_cnv_calling_v1.4.0. The app completed successfully without any error.
