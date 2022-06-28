# Pan4990 logfile
This is a VCP1 R119 test BED file for CNV analysis using ExomeDepth. It includes exon padding +/- 30pb and the 5'UTR padded 30bp.

## Request form
move request form to correct folder and rename to include Pan4990
`mv RequestForms/R119\ CNV\ DOC333_BEDfile_request_form.csv RequestForms/Pan4990_R119_CNV_BEDfile_request_form.csv`

## Transcripts
Pan4990_transcripts.txt file made manually using information from request form

## Run mokabed
`dx run project-ByfFPz00jy1fk6PjpZ95F27J:applet-FfjkPy80Vy31YK619YK1Yf4x -itranscript_file=project-GBxFZvQ0j2pZJJ8x50Q5Kq0x:file-GBxPF1Q0j2pq3zbX4xY18gfX -icoding_up=30 -icoding_down=30 -iup=30 -igenes_or_transcripts=TRANSCRIPTS -imergeboundaries=false`

### mokabed outputs:
command (see logfile for more details):
`/home/dnanexus/mokabed/LiveBedfiles/TestArea_for_bed_generation_script/OOBed7_uses_mirrored_database_.py --codingup 30 --codingdown 30 --up 30 --useaccessions --transcripts /home/dnanexus/in/transcript_file/Pan4990.txt --minuschr --outputfile /home/dnanexus/out/Output_files/Pan4990data.bed --logfile /home/dnanexus/out/Output_files/Pan4990_LogFile.txt `

outputs downloaded Pan4990_LogFile.txt and Pan4990data.bed

## Add Pan3608
`cat Pan3608.bed >> Pan4990data.bed`

## Sort and rename
`sort Pan4990data.bed -k1,1V -k2,2n -k3,3n > Pan4990_sorted.bed;mv Pan4990data.bed Pan4990_unsorted.bed; mv Pan4990_sorted.bed Pan4990data.bed; rm Pan4990_unsorted.bed`

## remove header
manually removed headers from Pan4990data.bed
