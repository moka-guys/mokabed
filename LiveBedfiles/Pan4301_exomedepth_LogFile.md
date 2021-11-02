This BED file is used for Exomedepth on VCP2 panel. It contains the numbered and unpadded meta-exons. Meta-exons are built from the overlap of exons with the capture regions and collapsed to build a virtual transcript that contains all exons of the collapsed transcripts.

## Process to build exomdepth capture file

1) Convert the capture BED to BED4 format 
        cut -f1-4 Pan4301data.bed > Pan4301capture.bed