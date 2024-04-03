# Pan5220
This bedfile will be used to perform the variant filtering step of exome depth for R79. It is a remake of Pan5168; it is a known issue that mokabed mapps exon 44 of LAMA2 incorrectly. While this issue was manually rectified in the VCP3 readcount bedfile (Pan5217), it was not corrected in Pan5168.

This bedfile will be a copy of Pan5168 but the LAMA2 region corrected.

# Take a copy of Pan5168
cp Pan5168_CNV.bed Pan5220_CNV.bed