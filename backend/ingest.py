# ingest text files from a folder into a vector store
# run manually once to populate the vector store
# after that, the chroma client in vectorstore.py will persist

import os
from vectorstore import add_documents

CHUNK_SIZE = 500

def ingest_folder(folder_path="data/"):
    print("Starting ingestion.")
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            print(f"Ingesting {filename}.")
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                text = f.read()
            chunks = [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
            ids = [f"{filename}_{i}" for i in range(len(chunks))]
            add_documents(chunks, ids)
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_folder("data/")
