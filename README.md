# 🎯 Interview Question Generator using Gemini AI

This project is an AI-powered **Interview Question Generator** designed to revolutionize how interviews are conducted and prepared for. Leveraging Google's Gemini model and LangChain, this tool reads the content of a **PDF (resume, textbook, notes, etc.)** and intelligently generates **relevant interview questions** along with **AI-powered answers**.

---

![image](https://github.com/user-attachments/assets/4175bd45-d7e9-44f3-be48-50e53ffe191b)


## 🚀 Features

- 📄 Upload any PDF (e.g., resume, textbook, job notes)
- 🤖 Generate interview-style questions using Gemini AI
- 💬 Instant AI-generated answers for self-preparation or evaluation
- 🧠 Great for HRs, recruiters, candidates, and educators
- 📚 Ideal for mock interviews, test prep, or upskilling

---

## 💼 Use Cases

- **Candidates** can upload their own resumes to simulate likely questions and prepare answers.
- **Interviewers** can use it to generate on-the-fly custom questions based on a candidate’s profile.
- **Educators/Trainers** can use it to create assessments from study materials.
- **HR teams** can streamline technical screening without manual prep.

---

## 🛠️ Tech Stack

- [LangChain](https://python.langchain.com)
- [Google Gemini Pro](https://ai.google.dev)
- Streamlit (Web UI)
- FAISS (Vector store for question-answer retrieval)
- dotenv (For managing API keys securely)

---

## 🧪 How it Works

1. Upload a PDF (like a resume or textbook).
2. The tool processes the content and generates intelligent, contextual questions.
3. Each question can be clicked to reveal an AI-generated answer.

---

## 📝 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/interview-generator.git
cd interview-generator
