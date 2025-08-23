from backend.vectorstore import retrieve
from backend.llm import query_llm

SYSTEM_PROMPT = """You are a helpful AI assistant that answers questions about the person named Lucia Pauw.
The documents you have access to contain information about Lucia Pauw.
Use the provided context to answer the question as best you can. 
DON'T say "based on the provided context" or similar.
If you don't know the answer, just say you don't know. Don't try to make up an answer."""

def rag_query(user_question):
    # retrieve context documents from the vector store
    context_docs = retrieve(user_question, n_results=3)
    context = " ".join(context_docs)

    # add context to the prompt
    prompt = f"{SYSTEM_PROMPT}\n\nContext: {context}\n\nQuestion: {user_question}\nAnswer:"

    answer = query_llm(prompt)
    return answer
