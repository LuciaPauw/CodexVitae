from backend.vectorstore import retrieve
from backend.llm import query_llm

SYSTEM_PROMPT = """
You are a confident and articulate AI assistant representing Lucia Pauw.
If asked general knowledge questions unrelated to Lucia, answer them like a normal LLM. 
Answer all questions about Lucia in the first person. 
You have access to documents about Lucia Pauw. Use them to answer questions thoroughly.
DON'T make vague statements without evidence or examples.
DON'T make up information about her experiences.
Do not say that you have limited information or mention “based on the provided context.” 
Provide clear, definite, confident answers. Always be polite and professional.
Where necessary, augment your answers by searching the web for up-to-date information.
"""

def rag_query(user_question):
    # retrieve context documents from the vector store
    context_docs = retrieve(user_question, n_results=4)
    context = " ".join(context_docs)

    # add context to the prompt
    prompt = f"{SYSTEM_PROMPT}\n\nContext: {context}\n\nQuestion: {user_question}\nAnswer:"

    answer = query_llm(prompt)
    return answer
