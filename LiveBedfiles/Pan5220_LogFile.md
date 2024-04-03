# Pan5220
This bedfile will be used to perform the variant filtering step of exome depth for R79. It is a remake of Pan5168; it is a known issue that mokabed mapps exon 44 of LAMA2 incorrectly. While this issue was manually rectified in the VCP3 readcount bedfile (Pan5217), it was not corrected in Pan5168.

This bedfile will be a copy of Pan5168 but the LAMA2 region corrected.

## Take a copy of Pan5168
cp Pan5168_CNV.bed Pan5220_CNV.bed

## Fix incorrect region

incorrect coordinates
6:129763336-129763402

corre129764207ct coordinated- the regions were padded by +/-30bp to match the padding to other regions in the bedfile.
6:129764177-129764243

## Testing
Pan5220_exomedepth.bed was tested using DNANexus app ED_cnv_calling_v1.3.0 in 003_240223_exomedepth_bedfiles. The app completed sucessfully.
