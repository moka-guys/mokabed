import pandas as pd

# Load the first CSV file
missing_regions = '_Pan5211_missed.bed'
df1 = pd.read_csv(missing_regions)

# Load the second CSV file
all_transcripts = '/home/natasha/Desktop/mokabed/LiveBedfiles/Transcripts/Pantranscriptfiles/Pan5211_alltranscripts.csv'
df2 = pd.read_csv(all_transcripts)

# Specify the common column to join on
common_column = 'Gene'

# Perform the join (inner join by default)
merged_df = pd.merge(df1, df2, on=common_column)

# Save the merged DataFrame to a new CSV file
merged_file = 'merged_file.csv'
merged_df.to_csv(merged_file, index=False)

#Load file with strand information
strand_info = '_Pan5211_6col.bed'
df3 = pd.read_csv(strand_info)

# Load file created in first merge
df4=pd.read_csv(merged_file)

common_column_final = 'Transcript'
columns_to_merge_from_df3 = ['Transcript','accession', 'strand']

# Perform the join and select specific columns from df1
join_type = "left"
merged_df_final = pd.merge(df4, df3[columns_to_merge_from_df3], on=common_column_final, how=join_type)

# Save the merged DataFrame to a new CSV file
merged_file_final = 'merged_file_final.csv'
merged_df_final.to_csv(merged_file_final, index=False)

print(f"Data from {strand_info} and {merged_file_final} has been merged, and selected columns from df1 have been included in {merged_file_final}.")
