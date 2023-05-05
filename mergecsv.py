import pandas as pd

# List the names of the CSV files to merge
file_names = ['word_embeddings_1.csv', 'word_embeddings_2.csv', 'word_embeddings_3.csv', 'word_embeddings_4.csv', 'word_embeddings_5.csv', 'word_embeddings_6.csv', 'word_embeddings_7.csv', 'word_embeddings_8.csv']

# Create an empty list to hold the pandas DataFrames for each file
dfs = []

# Loop through each file and read it into a pandas DataFrame, then append it to the list
for file_name in file_names:
    df = pd.read_csv(file_name)
    dfs.append(df)

# Concatenate the DataFrames in the list along the row axis to create one large DataFrame
merged_df = pd.concat(dfs, axis=0)

# Save the merged DataFrame to a CSV file
merged_df.to_csv('merged_file.csv', index=False)
