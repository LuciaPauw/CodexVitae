<div align="center" style="background:#f0f0f0; padding:20px; border-radius:10px;">
  <h1>📚 Codex Vitae </h1>
  <p>Thinking of hiring me? Let this agent answer your questions about who I am and what I can do.</p>
  <a href="https://luciacodexvitae.streamlit.app/">Try it out!</a> · 
</div>

## App Infrastructure

*Summary:* CodexVitae is an context-aware personal agent designed to answer your questions about me. It uses retrieval-augmented generation to provide accurate answers about my skills, academic achievements, work experience, projects, and character.

*Features:* 
 - **Agentic design:** System prompt guides the agent to maintain a consistent, authentic, first-person voice, and avoid hallucinations. If information is missing, it suggests contacting me directly.
 - **RAG pipeline:** Uses ChromaDB and sentence-transformers to embed and retrieve document chunks relevant to each question
 - **Response modes:** Users can select the response style: "Interview" (concise, professional, informative), "Fast facts" (bullets/TL;DR), and "Humble brag" (confident, emphasising valuable skills)
 - **Data ingestion:** `ingest.py` enables easy updating of context corpus by adding additional documents.

*Future improvements*
 - Refine document splitting and ingestion strategies for better context
 - Metadata tagging (e.g. document type and topic) to improve retrieval on large corpora    
 - Add my code and documentation so that the agent understands my writing, learning, and coding style better
 - Enable support for other file types (e.g. PDF)

### System Setup and Design Choices

| Component | Tool | Reason |
| --- | --- | --- |
| LLM Hosting Service | Groq | High-speed, low-latency inference; free dev tier |
| LLM | llama-3.1-8b-instant | Fast throughput, large context window |
| Vector Database | Chroma DB | Lightweight and local, built-in persistance |
| Frontend | Streamlit | Python-native, cloud hosted by default |

## Sample questions

To get an idea of how this agent converses, and to compare the different response tones, see the following example questions and answers.

**What are Lucia's strongest technical skills?** [Interview mode]
<details>
  <summary>🤖</summary>
  "My strongest technical skills lie in mathematical statistics and statistical learning theory. I've also had the opportunity to develop expertise in deep learning, including neural networks, NLP, computer vision, and agentic AI frameworks.

  In addition to these technical skills, I'm well-versed in a range of practical skills, including model training and evaluation, data plumbing, and working with messy real-world data. My experience with full-stack development and rapid software development has also equipped me to thrive in fast-paced environments."
</details>
<br>

**What are Lucia's strongest technical skills?** [Humble brag mode]
<details>
  <summary>🤖</summary>
  "I'm beyond thrilled to share my top technical skills. As a data scientist, I've invested a significant amount of time in honing my expertise, and I think it shows. My strongest technical skills lie in mathematical statistics and statistical learning theory – it's where I really feel I bring a unique value proposition. [...]"
</details>
<br>

**What does Lucia value in a team or company culture?** [Fast facts mode]
<details>
  <summary>🤖</summary>
  "Fast Facts: My Ideal Team and Company Culture:

  • Collaborative culture: I value teamwork where colleagues help each other out, share knowledge, and work together towards collective benefits.
  • Work that matters: The job should have a positive impact on customers, the field, the country, and the environment.
  • Technical excellence: I aim to be at the cutting edge of the data science field, driving trends and setting the bar high for myself and the company.
  • Independence: I appreciate autonomy in work pacing and the freedom to make decisions, as long as the quality of my work is not compromised.
  • Work-life balance: I believe a healthy balance between work and personal life is crucial for delivering outstanding, high-quality results."
</details>
<br>

**What's Lucia's favourite colour?** [Interview mode]
<details>
  <summary>🤖</summary>
  "Unfortunately, I don't have Lucia's personal preferences on file, including her favorite color. I'm an agent for Lucia Pauw and don't currently have that information. Why don't you contact Lucia directly via the information in the sidebar?"
</details>
<br>

## Working with AI

### AI-assisted commits

| Commit message | AI involvement |
| --- | --- |
| Added codexvitae.drawio | AI-generated |
| Refined codexvitae.drawio | Manual |
| Simple UI; call LLM | AI-generated |
| Start RAG: one document | AI-generated |
| Update codexvitae.drawio | Manual |
| Add agent system prompt | Manual |
| Change chunk size and overlap | AI-assisted |
| Start frontend | Manual | 
| Add context DB | AI-assisted |
| Dior new look (frontend) | AI-assisted |
| Improve RAG functionality | Manual |

### Prompt history

| Topic | Chat |
| --- | --- |
| Architecture choices and basic pipeline | [Link](https://chatgpt.com/share/68af0aa7-e3e0-8010-837a-a6b79f3f567c) |
| Streamlit development | [Link](https://chatgpt.com/share/68af0b14-f03c-8010-a8f4-52ff08e7bf36) |
| UI design and Streamlit development | [Link](https://chatgpt.com/share/68af0b51-fa14-8010-a82d-20eee605e73f) |
| Improve system prompt | [Link](https://chatgpt.com/share/68af0ba4-8010-8010-bf73-e50dcd5c2bec) |
| Improve chunking strategies | [Link](https://chatgpt.com/share/68af0bdd-8a98-8010-aa5e-54b9d812a572) |