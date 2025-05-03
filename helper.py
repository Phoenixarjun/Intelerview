from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from prompt import prompt_template



load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

fila_path = "./data/Machine Learning for Absolute Beginners.pdf"


def file_processing(file_path):
  loader = PyPDFLoader(file_path)
  documents = loader.load()

  question_gen = ""
  for page in documents:
    question_gen += page.page_content 

  text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=10000,
    chunk_overlap=200
  )

  chunks = text_splitter.split_text(question_gen)

  documents_ques_gen = [Document(page_content=chunk) for chunk in chunks]

  text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=1000,
    chunk_overlap=200
  )

  document_answer_gen = text_splitter.split_documents(documents_ques_gen)

  return documents_ques_gen, document_answer_gen


def llm_pipeline(file_path):
  documents_ques_gen, document_answer_gen = file_processing(file_path)

  llm = GoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.2, api_key=os.environ["GEMINI_API_KEY"])

  PROMPT_QUESTIONS = PromptTemplate(template=prompt_template, input_variables=["text"])

  ques_gen_chain = LLMChain(llm=llm, prompt=PROMPT_QUESTIONS, verbose=True)

  ques = ques_gen_chain.run(documents_ques_gen)

  embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
  )

  vectorstore = FAISS.from_documents(document_answer_gen, embeddings)

  llm_answer = GoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.2, api_key=os.environ["GEMINI_API_KEY"])

  ques_list = ques.split("\n")
  filtered_ques_list = [ques for ques in ques_list if ques.endswith("?") or ques.endswith(".")]

  answer_generation_chain = RetrievalQA.from_chain_type(
    llm=llm_answer,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
  )

  return answer_generation_chain, filtered_ques_list

