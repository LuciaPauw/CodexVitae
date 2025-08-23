# streamlit entry point
import streamlit as st
from backend.rag_pipeline import rag_query

st.set_page_config(
    page_title="Codex Vitae"
)

st.image("./static/1.png", use_container_width=True)

# col1, col2, col3 = st.columns([1, 3, 1])
# with col2:
#     st.image("./static/2.png", width=800)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.text("Thinking of hiring me? Let this agent answer your questions about who I am and what I can do.")


user_question = st.text_input("Ask away!")

if st.button("Submit") and user_question:
    with st.spinner("Generating answer..."):
        answer = rag_query(user_question)
    st.write("### Answer")
    st.write(answer)