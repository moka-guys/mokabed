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

## convert to 4 column format
`cut -f 1-4 Pan4990data.bed > Pan4990data_4col.bed; rm Pan4990data.bed; mv Pan4990data_4col.bed Pan4990data.bed`

## Rename to make clear it's a CNV BED file
`mv Pan4990data.bed Pan4990_CNV.bed`

## Testing
Tested in 003_220628_Pan4988_Pan4989_Pan4990 with exome depth
`dx run project-G8v9kbj0bfZ7vzYy5byGXGFX:applet-G8xQVQ80bfZ2kvGV1bPbBvQv -iproject_name=003_220321_ED_cnv_calling_v1.1.0 -ireadcount_file=project-G8v9kbj0bfZ7vzYy5byGXGFX:file-G9QZK100qZgVZybY4g387255 -ibamfile_pannumbers="Pan4119,Pan4044" -iQC_file=project-G8v9kbj0bfZ7vzYy5byGXGFX:file-G8xKgZ80bfZ5zpJ0F4xb90xb -isubpanel_bed=project-GBxFZvQ0j2pZJJ8x50Q5Kq0x:file-GBxPQv00j2pzG67YK2Pg4543`

Job completed without error