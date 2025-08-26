# streamlit entry point
import streamlit as st
from backend.rag_pipeline import rag_query

st.set_page_config(
    page_title="Codex Vitae"
)

# sidebar
st.sidebar.image("./static/1.png", use_container_width=True)

st.sidebar.markdown(
    """
    <div style="background-color:#dbe4f0; padding: 1rem; 
                border-radius: 8px; margin-bottom: 1rem;
                color: #304674;">
        <b>Personal brand promise</b><br>
        I am committed to excellence in data science, AI, and entrepreneurship.<br>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.image("./static/Pauw.png", use_container_width=True)

# main panel
col1, col2 = st.columns([1, 4])
with col1:
    st.image("./static/chatbot2.png", width=200)
with col2:
    st.subheader("Thinking of hiring me?")
    st.text("Let this agent answer your questions about who I am and what I can do.")

st.markdown(
    """
    <style>
        .stTextInput input {
            background-color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
user_question = st.text_input("Ask away!", placeholder="E.g. What are Lucia's strongest technical skills?")

if st.button("Submit") and user_question:
    with st.spinner("Generating answer..."):
        answer = rag_query(user_question)
    st.write("### Answer")
    st.write(answer)