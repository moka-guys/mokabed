# Generate exomdepth targets BED from a set of known capture regions
All exons are numbered as meta-exons and only include coding sequence.

## Generating the BED file for Exomedepth
./makeExomedepth.sh hg19 output Pan4361.bed Pan4362_extra.bed
                    |    |      |           |
                    |    |      |           +- additional exons (not included in UCSC dataset)
                    |    |      +- the capture (BED4 format)
                    |    +- output file name root
                    +- the ucsc database (assembly) to use for annotation retrieval

## Output files
output.genepred.hg19 - GenePred RefGene from UCSC (suffixed by database id)
output.chromosomes - UCSC-Ensembl chromosome mappings
output.genepred - GenePred RefGene with Ensembl chromosome names
output.bed - RefGene in BED12 format
output_cdsexons.bed - Coding exons (RefGene)
output_captureexons.bed - Exons that intersect capture regions
output_metaexons.bed - The built meta-exon set
output_exomedepth.bed - Numbered exons for ExomeDepth
