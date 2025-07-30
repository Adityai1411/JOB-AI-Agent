

```markdown
# 🤖 JOB-AI-Agent

An intelligent AI agent built with LLMs to analyze and interact with job descriptions. This Streamlit-based app enables smart insights from structured and unstructured job data using modern LLM APIs.

---

## 🚀 Features

- 🔍 **Job Description Parsing** – Upload and analyze `.json` or text-based job descriptions  
- 🧠 **LLM-Powered Agent** – Uses LLM (via Groq API) for deep natural language understanding  
- 📊 **Streamlit UI** – Intuitive and interactive web interface  
- 🔐 **Secure Config** – Uses `.streamlit/secrets.toml` to store API keys securely (not pushed to GitHub)  

---

## 📁 Project Structure



job\_descriptions/
├── .streamlit/
│   └── secrets.toml         # API keys (do not commit this file)
├── 30company new----.json   # Sample job descriptions
├── llm.py                   # Core logic using LLM
├── stm\_agnt.py              # Streamlit agent handler
├── streamlit\_llm.py         # Main Streamlit entry point
├── README.md                # Project documentation

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Adityai1411/JOB-AI-Agent.git
cd JOB-AI-Agent
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Secrets File

Create a file named `.streamlit/secrets.toml` and add your Groq API key:

```toml
[GROQ]
api_key = "your-groq-api-key-here"
```

⚠️ **DO NOT** commit this file to GitHub. Use `.gitignore`.

---

## ▶️ Run the App

```bash
streamlit run streamlit_llm.py
```

---

## 📌 Future Improvements

* [ ] PDF/DOCX support for job descriptions
* [ ] Resume parsing and JD matching
* [ ] Multi-agent collaboration features
* [ ] Export analysis as PDF or CSV

---

## 💡 Purpose

This tool was built to automate the analysis of job descriptions using cutting-edge LLM capabilities — saving time for recruiters, job seekers, and career coaches.

---

## 👤 Author

**Aditya Ingale**
🔗 [GitHub](https://github.com/Adityai1411)

---



```

---

