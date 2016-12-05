'''
Created on 2 Dec 2016

@author: kevin
'''

import cruzdb, os
import pandas as pd

def refgenelist():
    
    ###################################### Generate list of NM gene symbols includes genes for which there exist NR accessions also #############
    g = cruzdb.Genome(db='hg19')
    ##Returns all Gene symbols in name2 column (this contains repeats and non-coding gene symbols)
    df_raw = g.dataframe('refGene')
    #Generate a subset of dataframe containing just the chr1-22,X and Y 
    df = df_raw.loc[df_raw['chrom'].isin(['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY'])].copy()
    
    #####Generate a list of true false values indicating the presence or absence of an NM accession string in the name column
    df['Boolean_NMaccessions'] = df.name.str.contains(pat='NM_')
    #####Generate a df which contains only those rows which contain a NM accession in the name column
    df4 = df[df['Boolean_NMaccessions'] == True]
    #####Remove duplicate gene symbol names
    df5 = df4.drop_duplicates('name2')
    
    
    #####Return just the Gene Symbol list
    df6 = pd.DataFrame(zip(df5['name2']),  columns = ["GeneSymbol"])
    ##### Concatanate Gene Symbol list with empty Accession column
    df7 = pd.concat([df6, pd.DataFrame(columns=['Accession'])])
    ##### Re-index data frame so that GeneSymbol column is the index
    df7_reindex = df7.reindex(columns=['Accession'], index=[df6['GeneSymbol']])
    
    df7_reindex.index.name = "GeneSymbol"
    
    ##### Write the list of GeneSymbols to a text file
    #df7_reindex.to_csv(path_or_buf='/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/RefGene_gene_list_2016_12_02/RefGene_Gene_symbols_removeduplicates_NMaccessionGenes_Pan468.csv', sep='\t')
    df7_reindex.to_csv(path_or_buf='/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan468.txt', sep='\t')

    
     
    
    ################### Verify that all coding regions have been captured by  running the code below #######################################

    df['Boolean'] = df['cdsEndStat'].str.contains(pat='cmpl')
    
    df2 = df[df['Boolean'] == True]
    
    df3 = df2.drop_duplicates('name2')
    
    #####Calculate the number of entries relating to gene symbols containing NM accessions
    #logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/RefGene_gene_list_2016_12_02/refgenelist_log.txt", "w+")
    logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan468_Pan492_Pan493_refgenelist_log.txt", "w+")
    logger.write("Total number of coding gene entries (counts number of NM accessions) in RefGene table = " + str(len(df5[df5['Boolean_NMaccessions'] == True])) + "\n")
    logger.write("Alternative method to generate total number of coding gene entries (counts number cdsEndStat entries = cmpl) of cds in RefGene table = " + str(len(df3[df3['Boolean'] == True])) + "\n")
   
    logger.close()
    
        
    ###################################### Generate list of NR gene symbols includes genes for which there exist NM accessions also #############
    
    ##### Return True value if NR_ accession present otherwise return False
    df['Boolean'] = df['name'].str.contains(pat='NR_')
    
    ##### Generate a df which contains only those rows which contain a NR accession in the name column
    df8 = df[df['Boolean'] == True]
    
    ##### Remove duplicate gene symbol names
    df9 = df8.drop_duplicates('name2')
    #####Return just the Gene Symbol list
    df10 = pd.DataFrame(zip(df9['name2']),  columns = ["GeneSymbol"])
    ##### Concatenate Gene Symbol list with empty Accession column
    df11 = pd.concat([df10, pd.DataFrame(columns=['Accession'])])
    ##### Re-index data frame so that GeneSymbol column is the index
    df11_reindex = df11.reindex(columns=['Accession'], index=[df11['GeneSymbol']])
    
    df11_reindex.index.name = "GeneSymbol"
    
    ##### Write the list of GeneSymbols to a text file
    #df11_reindex.to_csv(path_or_buf='/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/RefGene_gene_list_2016_12_02/RefGene_Gene_symbols_removeduplicates_NRaccessionGenes.csv', sep='\t')


    ################### Verify that all non-coding regions have been captured by running the code below #######################################

    df['Boolean_alternative'] = df['cdsEndStat'].str.contains(pat='unk')

    df12 = df[df['Boolean_alternative'] == True]
    
    df13 = df12.drop_duplicates('name2')
    
    len(df13[df13['Boolean_alternative'] == True])
    
    #####Calculate the number of entries relating to non-coding gene symbols
    #logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/RefGene_gene_list_2016_12_02/refgenelist_log.txt", "a+")
    logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan468_Pan492_Pan493_refgenelist_log.txt", "a+")
    logger.write("Total number of non-coding gene entries (counts number of NR accessions) in RefGene table = " + str(len(df9[df9['Boolean'] == True])) + "\n")
    logger.write("Alternative method to generate total number of non-coding gene entries (counts number cdsEndStat entries = unk) in RefGene table = " + str(len(df13[df13['Boolean_alternative'] == True])) + "\n")
                                                                                                                
    logger.close()
    
    ###################################### Generate list of NR gene symbols does not include genes for which there exist NR accessions also #############
       
    # df column indicating True for Genes with NM and NR accessions and False otherwise
    df10['BooleanTrueNRNM'] = df10['GeneSymbol'].isin(df6['GeneSymbol'])
    # df containing just genes which have an NR accession but no corresponding NM accession
    dfNR_minusNMgenes = df10.loc[df10['BooleanTrueNRNM'] == False]
    
    ##### Concatenate Gene Symbol list with empty Accession column
    dfNR_minusNMgenes = pd.concat([dfNR_minusNMgenes, pd.DataFrame(columns=['Accession'])])
    ##### Re-index data frame so that GeneSymbol column is the index
    dfNR_minusNMgenes_reindex = dfNR_minusNMgenes.reindex(columns=['Accession'], index=[dfNR_minusNMgenes['GeneSymbol']])
    dfNR_minusNMgenes_reindex.to_csv(path_or_buf='/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan492.txt', sep='\t')
    
        
    
    # Merge df7 (list of genes which contain a NM accession or a NM and NR accession) merged with df11 (list of genes containing NR or NM and NR accesion)
    # This merge returns just the genes which have both NM and NR accessions
    dfmerge = pd.merge(df7, df11, on=["GeneSymbol"], how='inner')
    
    
    
        
    #logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/RefGene_gene_list_2016_12_02/refgenelist_log.txt", "a+")
    logger = open("/run/user/1000/gvfs/sftp:host=athena.kcl.ac.uk,user=ryank/home/ryank/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan468_Pan492_Pan493_refgenelist_log.txt", "a+")
    logger.write("Breakdown of gene symbols with NR accessions \n.Total number of coding gene entries in RefGene table with a non-coding accession = " + str(len(dfmerge)) + "\n")
    logger.write("Total number of gene entries in RefGene table with a non-coding accession and no corresponding NM accession = " + str(len(dfNR_minusNMgenes_reindex)) + "\n")
    if (len(dfNR_minusNMgenes_reindex) + len(dfmerge)) == len(df9[df9['Boolean'] == True]):
        logger.write("The number of NR related genes tally:" + " " + str(len(dfNR_minusNMgenes_reindex)) + " + " + str(len(dfmerge)) + " = " + str(len(df9[df9['Boolean'] == True])) + "\n")
    else:
        logger.write("ERROR the number of NR related genes do not tally check the number of genes which just have NR accessions only plus genes which have NM and NR accessions equal the total number of genes which have a NR accession\n")
                                                                                                     
    logger.close()
    
    
    
    return len(dfNR_minusNMgenes_reindex), len(dfmerge), len(df9[df9['Boolean'] == True])
     


    
    
if __name__ == '__main__':
    print refgenelist()