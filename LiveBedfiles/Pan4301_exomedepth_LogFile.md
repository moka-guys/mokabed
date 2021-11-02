This BED file is used for Exomedepth on VCP2 panel. It contains the numbered and unpadded meta-exons. Meta-exons are built from the overlap of exons with the capture regions and collapsed to build a virtual transcript that contains all exons of the collapsed transcripts.

## Process to build exomdepth capture file

1) Convert the capture BED to BED4 format 
        cut -f1-4 Pan4301data.bed > Pan4301capture.bed

2) Run the makeExomedepth script to identify capture regions not part of the UCSC RefGene Set

        bash TestArea_for_bed_generation_script/makeExomedepth.sh hg19 tmp Pan4301capture.bed

3) Manually edit tmp_missed.bed to use gene symbol as 4th column. Add 0 and strand info in 5th and 6th column

4) Remove padding on added coding exon in tmp_missed.bed. Since the BRCA1 region is only 11 bp, therefore no padding to remove.

5) Rename the edited file to Pan4301_extra.bed.

        mv tmp_missed.bed Pan4301_extra.bed

6) Run makeExomedepth to generate final exomdepth BED file (Pan4301_exomdepth.bed)
        bash TestArea_for_bed_generation_script/makeExomedepth.sh hg19 Pan4301final Pan4301capture.bed Pan4301_extra.bed 

        inputs
        - the ucsc database (assembly) to use for annotation retrieval
        - output file name
        - the capture (BED4 format)
        - additional exons (not included in UCSC dataset)

7) Ensure no regions are reported as missed and Pan4301final_missed.bed is empty.

8) Remove any tmp files
        rm *tmp*

9) Remove unrequired intermediate files
        rm Pan4301_extra.bed Pan4301final_captureexons.bed Pan4301final_cdsexons.bed Pan4301final.chromosomes Pan4301final.genepred Pan4301final_metaexons.bed Pan4301final_cdsexons.bed Pan4301final.genepred.hg19 Pan4301final_missed.bed

10) Rename final BED file
        mv Pan4301final_exomedepth.bed Pan4301exomedepth.bed


## Remove overlapping region
    The script added a region (TOE1_1:45805924-45805976) not required for VCP2 as it was overlapping with MUTYH_1
    Manually removed that region from Pan4301exomedepth.bed


