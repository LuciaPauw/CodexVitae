# streamlit entry point
import streamlit as st
from backend.rag_pipeline import rag_query

st.set_page_config(
    page_title="Codex Vitae"
)
st.image("./static/banner.png", use_container_width=True)

st.title("Lucia Pauw")
st.subheader("Codex Vitae")

user_question = st.text_input("Ask a question:")

if st.button("Submit") and user_question:
    with st.spinner("Generating answer..."):
        answer = rag_query(user_question)
    st.write("### Answer")
    st.write(answer)