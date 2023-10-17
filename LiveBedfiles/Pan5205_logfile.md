# Pan5205 
This bedfile is for TSO500 coverage calculations.
It replaces the previous bedfile Pan5130, and is based on that file.
When Pan5130 was introduced it was noticed that two regions in BRAF were included in the bedfile that are not present in the capture. This results in low coverage which must be checked for every sample requiring BRAF analysis, which adds time to the analysis. The additional regions are exons from the MANEPlusClinical transcript NM_001374258.1:

chr7	140426283	140426326	7-140426283-140426326	0	+	BRAF;NM_001374258.1	673
chr7	140485478	140485618	7-140485478-140485618	0	+	BRAF;NM_001374258.1	673

This new bedfile will be made by deleting the regions from the existing Pan5130.
