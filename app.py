from flask import Flask, request, render_template
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
import pinecone
import config

app = Flask(__name__)

openai.api_key = config.OPENAI_API_KEY
pinecone.init(api_key=config.PINECONE_API_KEY, environment='northamerica-northeast1-gcp')

INDEX_NAME = config.PINECONE_INDEX_NAME

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

@app.route('/')
def search_form():
    return render_template('search_form.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    search_term_vector = get_embedding(query, engine="text-embedding-ada-002")
    index = pinecone.Index(INDEX_NAME)
    results = index.query(search_term_vector, top_k=3, include_metadata=True)
    matches = results['matches']
    texts = []
    for match in matches:
        if 'metadata' in match:
            metadata = match['metadata']
            if 'text' in metadata:
                text = metadata['text']
                texts.append(text)

    

    return render_template('search_results.html', query=query, results=texts)


if __name__ == '__main__':
    app.run()
