from backend.vectorstore import retrieve
from backend.llm import query_llm

def rag_query(user_question):
    # retrieve context documents from the vector store
    context_docs = retrieve(user_question, n_results=3)
    context = " ".join(context_docs)

    # add context to the prompt
    prompt = f"Use the following context to answer the question.\n\nContext: {context}\n\nQuestion: {user_question}\nAnswer:"

    answer = query_llm(prompt)
    return answer
