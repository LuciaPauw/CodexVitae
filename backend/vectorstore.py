import os
import chromadb
from chromadb.utils import embedding_functions

os.environ["TOKENIZERS_PARALLELISM"] = "false"

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="docs",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
)

def add_documents(docs, ids):
    collection.add(documents=docs, ids=ids)

def retrieve(query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0]
