import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('sentences.csv')

# Split the DataFrame into three chunks of 50 records each
dfs = [df[i:i+50] for i in range(0, len(df), 50)]

# Save each chunk to a separate CSV file
for i in range(len(dfs)):
    dfs[i].to_csv(f'output_file_{i+1}.csv', index=False)
