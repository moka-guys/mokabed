# Pan4989
This is a VCP1 R117 test BED file for CNV analysis using ExomeDepth. It includes exon padding +/- 30pb and the 5'UTR padded 30bp

## Request form
Rename request form to include Pan4989
`mv RequestForms/R118\ CNV\ DOC333_BEDfile_request_form.csv RequestForms/Pan4989_R118_CNV_BEDfile_request_form.csv`

## Transcripts
Pan4989_transcripts.txt made manually using information from request form.

## Run mokabed
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=project-GBxFZvQ0j2pZJJ8x50Q5Kq0x:file-GBxK34Q0j2ppBFXX9P0j5J13 -icoding_up=30 -icoding_down=30 -iup=30 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

### mokabed outputs:
command (see logfile for more details):
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4989_transcripts.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4989_transcriptsdata.bed --logfile /home/dnanexus/out/Output_files/Pan4989_transcripts_LogFile.txt`

Outputs downloaded Pan4989_transcripts_LogFile.txt and Pan4989_transcriptsdata.bed

## Rename data.bed
`mv Pan4989_transcriptsdata.bed Pan4989data.bed`

## Add Pan3608
`cat Pan3608.bed >> Pan4989data.bed`

## Sort and rename
`sort Pan4989data.bed -k1,1V -k2,2n -k3,3n > Pan4989_sorted.bed;mv Pan4989data.bed Pan4989_unsorted.bed; mv Pan4989_sorted.bed Pan4989data.bed; rm Pan4989_unsorted.bed`

## remove header
manually removed headers from Pan4989data.bed

## convert to 4 column format
`cut -f 1-4 Pan4989data.bed > Pan4989data_4col.bed; rm Pan4989data.bed; mv Pan4989data_4col.bed Pan4989data.bed`

## Rename to make clear it's a CNV BED file
`mv Pan4989data.bed Pan4989_CNV.bed`

## Testing
Tested in 003_220628_Pan4988_Pan4989_Pan4990 with exome depth
`dx run project-G8v9kbj0bfZ7vzYy5byGXGFX:applet-G8xQVQ80bfZ2kvGV1bPbBvQv -iproject_name=003_220321_ED_cnv_calling_v1.1.0 -ireadcount_file=project-G8v9kbj0bfZ7vzYy5byGXGFX:file-G9QZK100qZgVZybY4g387255 -ibamfile_pannumbers="Pan4119,Pan4044" -iQC_file=project-G8v9kbj0bfZ7vzYy5byGXGFX:file-G8xKgZ80bfZ5zpJ0F4xb90xb -isubpanel_bed=project-GBxFZvQ0j2pZJJ8x50Q5Kq0x:file-GBxKFf80j2pkFv9YKB2pKX9b`

Job completed without error