import streamlit as st
from helper import llm_pipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

st.title("🎯Intelerview - Interview Question Generator")
st.write("Upload a PDF to generate interview questions and get answers using Gemini.")

st.sidebar.header("📄 Upload PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")
proceed_btn = st.sidebar.button("🚀 Process PDF")

if uploaded_file is not None:
    with open("uploaded_file.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success("✅ File uploaded successfully!")

    if proceed_btn:
        with st.spinner("Processing PDF with Gemini..."):
            answer_chain, questions = llm_pipeline("uploaded_file.pdf")

        st.success("✅ Questions Generated!")
        for i, question in enumerate(questions, 1):
            with st.expander(f"Q{i}: {question}"):
                answer = answer_chain.run(question)
                st.write(f"💡 {answer}")
