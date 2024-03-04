# Pan5213 

This BEDfile contains problematic single exon genes specific to VCP3. The genes were requested in a VCP3 request form, however the Mokabed app consistently excluded them from the final data.bed output.

Padding these single exon genes does not resolve this issue.

The genomic coordinates for these genes were obtained from UCSC using the RefSeq transcript information. The coordinates were independently checked by two Bioinformaticians (RH and NP).

The final BED file was loaded in UCSC as a custom track and each gene's location was compared again to RefSeq data to ensure it matched.

