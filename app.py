print("Starting the Streamlit app")

# streamlit entry point
import streamlit as st
from backend.llm import query_llm

st.title("📚 Minimal RAG Prototype")

user_question = st.text_input("Ask a question:")

if st.button("Submit") and user_question:
    with st.spinner("Generating answer..."):
        answer = query_llm(user_question)
    st.write("### Answer")
    st.write(answer)
