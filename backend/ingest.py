# ingest text files from a folder into a vector store
# run manually once to populate the vector store
# after that, the chroma client in vectorstore.py will persist
import os
import re
from vectorstore import add_documents

CHUNK_SIZE = 50
CHUNK_OVERLAP = 15

def split_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)
        chunks.append(chunk_text)
        start += chunk_size - overlap  # move start forward with overlap
    return chunks

def ingest_folder(folder_path="data/"):
    print("Starting ingestion.")
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            print(f"Ingesting {filename}.")
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                text = f.read()
            # normalise whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            chunks = split_into_chunks(text)
            ids = [f"{filename}_{i}" for i in range(len(chunks))]
            add_documents(chunks, ids)
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_folder("data/")
