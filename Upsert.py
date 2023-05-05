import pinecone
import config
import json

# Initialize Pinecone
pinecone.init(api_key=config.PINECONE_API_KEY, environment='northamerica-northeast1-gcp')

# Create or retrieve the index
index_name = config.PINECONE_INDEX_NAME
index = pinecone.Index(index_name)

# Load data from the JSON file
with open('output.json', 'r') as f:
    data = json.load(f)

# Upsert the data to the index
index.upsert(vectors=data)


