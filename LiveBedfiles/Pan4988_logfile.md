# Pan4988 Logfile
This is a VCP1 R117 test BED file for CNV analysis using ExomeDepth. It includes exon padding +/- 30pb and the 5'UTR padded 30bp

## Request form
move request form to correct folder and rename to include Pan4988
` mv R117\ CNV\ DOC333_BEDfile_request_form.csv RequestForms/Pan4988_R117_CNV_BEDfile_request_form.csv`

## Transcripts
Pan4988_transcripts.txt file made manually using information from request form
remade Pan4988_transcripts.txt file changing spaces for tabs.

## Run mokabed
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=project-GBxFZvQ0j2pZJJ8x50Q5Kq0x:file-GBxJ2V80j2px4xGQ04ppF4Y7 -icoding_up=30 -icoding_down=30 -iup=30 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

### mokabed outputs:
command (see logfile for more details):
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4988_transcripts.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4988_transcriptsdata.bed --logfile /home/dnanexus/out/Output_files/Pan4988_transcripts_LogFile.txt `

Outputs downloaded Pan4988_transcripts_LogFile.txt and Pan4988_transcriptsdata.bed
