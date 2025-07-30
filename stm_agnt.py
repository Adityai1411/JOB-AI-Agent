import streamlit as st
import pandas as pd
import PyPDF2
import docx
import json
from groq import Groq

st.set_page_config(page_title="AI Company Dashboard", layout="wide")
st.title("AI Company Insight Dashboard")

# === Groq API Setup ===
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
model_name = "llama3-70b-8192"
max_tokens = 2048

# === File Upload ===
uploaded_file = st.sidebar.file_uploader("Upload CSV, PDF, DOCX or JSON", type=["csv", "pdf", "docx", "json"])
document_text = ""

if uploaded_file:
    file_type = uploaded_file.type

    if file_type == "text/csv":
        df = pd.read_csv(uploaded_file)
        document_text = df.to_string(index=False)
        st.dataframe(df.head(50), use_container_width=True)

    elif file_type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            document_text += page.extract_text() or ""

    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            document_text += para.text + "\n"

    elif file_type == "application/json":
        json_data = json.load(uploaded_file)
        document_text = json.dumps(json_data, indent=2)
        st.json(json_data)

# === Chat Memory ===
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

# === User Input ===
prompt = st.text_input("Ask a question about the dataset:")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

# === Inject system context ===
if document_text and not any(msg["role"] == "system" for msg in st.session_state.messages):
    st.session_state.messages.insert(0, {
        "role": "system",
        "content": f"Use this company dataset to answer smartly:\n\n{document_text}"
    })

# === Chat Response ===
if len(st.session_state.messages) > 1:
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=model_name,
                messages=st.session_state.messages,
                max_tokens=max_tokens
            )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown("### Response:")
        st.write(reply)

    except Exception as e:
        st.error(f"Error: {e}")