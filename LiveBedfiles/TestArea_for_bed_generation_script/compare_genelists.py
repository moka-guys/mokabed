import sys
import pandas as pd

## Script compares genes listed in a BED file and genes listed in a BED file request form to identify missing genes.
## Input files have to be in csv format

def compare_columns(bedfile, transcriptfile, bedfile_column, transcriptfile_column):
    # Read CSV files into DataFrames
    df1 = pd.read_csv(bedfile)
    df2 = pd.read_csv(transcriptfile)

    # Extract the columns from the DataFrames
    column_data1 = set(df1[bedfile_column])
    column_data2 = set(df2[transcriptfile_column])

    # Find data missing in file 1
    missing_in_file1 = column_data2 - column_data1

    return missing_in_file1

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python compare_genelists.py bedfile, transcriptfile, bedfile_column, transcriptfile_column")
        sys.exit(1)

    bedfile = sys.argv[1]
    transcriptfile = sys.argv[2]
    column_to_compare_bedfile = sys.argv[3]
    column_to_compare_transcriptfile = sys.argv[4]

    missing_data = compare_columns(bedfile, transcriptfile, column_to_compare_bedfile, column_to_compare_transcriptfile)

    print("Genes missing:")
    print(missing_data)