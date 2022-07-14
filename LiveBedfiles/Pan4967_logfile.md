# Pan4967

Pan4967 is used to create a masked reference genome used for the LRPCR.

## Pan4967_reference.bed
To mask a reference genome we need to provide a BED file with all the regions that are to be masked.
Our starting point is the regions that we want to align to, ensuring reads do not map to pseudogenes.
Therefore to mask the reference we must make a complement BED file, containing everything apart from the regions we want to be left unmasked.
This does not require specific exons etc to be covered -  a single region per gene is sufficient.

Pan4967_reference.bed has been created using the primer sequences which was provided as below. Note that each gene has a single amplicon except for PMS2, where there are 3 overlapping amplicons.


|Primer name|sequence|coordinate|Amplicon coordinates|
| --- | --- | --- | --- |
|PMS2_NGS_F1_02_F|CCGCGCCCGACCTGGAAAGATACATA|chr7:6049625-6049650|chr7:6036325-6049650|
|PMS2_NGS_F1_02_R|TGAACTGCCTTCATCAGATGCCAGGA|chr7:6036325-6036350||
|PMS2_F2_F1|TCAGGCTGCTTTTAATTTCATGTG|chr7:6040147-6040170|chr7:6028355-6040170|
|PMS2_LR_Ex10_R_02|AATTTTGCCACATGACTTGGGTGA|chr7:6028355-6028378||
|PMS2_NGS_F3_04_F|AGCCCTTCCGTATTTTGTCTATTCA|chr7:6030089-6030113|chr7:6012820-6030113|
|LRPCR_Uni_R|ACACGAGCGCATGCAAACATAGAG|chr7:6012820-6012843||
|CHEK2_Ex10_15_LR_Fv3|GTTAGCTGGTTGAAGTGGCATGCTTTGTG|chr22:29093702-29093730|chr22:29082610-29093730|
|CHEK2_EX10_15_LR_Rv2|CATTTACCAGCTGTGCAACATCGGA|chr22:29082610-29082634||
|IKBKG_M_LR_F|CCCACCCACGTCACCCAGAATGATCT|chrX:153779710-153779735|chrX:153779710-153793317|
|IKBKG_M_LR_R|ATCGCCCATGCTCAGTGGTGTCACTT|chrX:153793292-153793317||
|SMN1_in1_15kb_F01|aggccggtttcctccatatgatcttgc|chr5:70233401-70233427|chr5:70233401-70248509|
|SMN_FL_ex8_R|CCCCCACCCCAGTCTTTTACAGATGGT|chr5:70248483-70248509||

## create Pan4967_reference.bed
Take a copy of the above table
