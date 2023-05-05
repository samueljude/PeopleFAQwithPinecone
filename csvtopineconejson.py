import pandas as pd
import json

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_csv_file.csv')

# Create a list to hold the data points
data_points = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    text = row['text']
    embeddings = [float(value) for value in row['embeddings'].strip('[]').split(', ')]

    # Create a dictionary for the data point
    data_point = {
        "id": f"item_{index}",
        "metadata": {"text": text},
        "values": embeddings
    }

    # Append the data point to the list
    data_points.append(data_point)

# Write the data points to a JSON file
with open('output.json', 'w') as f:
    json.dump(data_points, f, indent=2)
