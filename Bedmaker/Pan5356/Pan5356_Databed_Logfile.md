## Pan5356
This Pannumber is used for small variant calling/filtering bed file (i.e. data.bed)

## Copy Pan5347 to Pan5356
Existing small variant calling/filtering bed file is Pan5347_data.bed. To make additional changes, Pan5347 was copied into Pan5356

cp ../Pan5347/Pan5347_data.bed ./Pan5356_data.bed

## Extend the padding region 
BARD1 and MBD4 genes were added into CNV calling bed files for R208 and R211 respectively, that are VCP2 panels. For VCP2, +/-30 padding is needed, so for these genes, additional +/-20 padding was added manually

## testing
Updated bedfile was tested by running vcfeval_hap.py_v1.4.3 and filter_vcf_with_bedfile_v1.2.0 and the apps finished without error. 

## add 5UTR regions for MBD4 and BARD1
5UTR regions were added for MBD4 and BARD1 genes. The regions were manually copied from readcount bedfile. 

## manually trim the overlapping region
BARD1 and MBD4 gene were manually trimmed following the examples from BRCA1, BRCA2, MLH1, LDLR
For example:
17	41276003	41276113	899	BRCA1;NM_007294.4
17	41276113	41276132	899	BRCA1_5UTR;NM_007294.4
17	41277287	41277381	899	BRCA1_5UTR;NM_007294.4

13	32889644	32889804	104	BRCA2_5UTR;NM_000059.4
13	32890558	32890597	104	BRCA2_5UTR;NM_000059.4
13	32890597	32890694	104	BRCA2;NM_000059.4

3	37035008	37035038	867	MLH1_5UTR;NM_000249.4
3	37035038	37035184	867	MLH1;NM_000249.4

19	11200138	11200224	670	LDLR_5UTR;NM_000527.5
19	11200224	11200321	670	LDLR;NM_000527.5

## testing
Updated bed was tested by running vcfeval_hap.py_v1.4.3 and filter_vcf_with_bedfile_v1.2.0 and the apps finished without error