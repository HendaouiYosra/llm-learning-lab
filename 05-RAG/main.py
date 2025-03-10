from langchain_community.document_loaders import PyPDFLoader                   #used to extract text from pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter            #used to create small chunks of documents
from langchain_community.vectorstores import FAISS                             #used to create and search vector databases
from langchain_ollama import OllamaEmbeddings                                  #used to create embedding(vectors)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM                                    #used to load model
import os
pdfs_directory = 'pdfs/'
os.makedirs(pdfs_directory, exist_ok=True)  


embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")

model = OllamaLLM(model="deepseek-r1:1.5b")

template = """
You are an assistant that answers questions. Using the following retrieved information, answer the user question. If you don't know the answer, say that you don't know. Use up to three sentences, keeping the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

def upload_pdf(file):
    file_path = os.path.join(pdfs_directory, file.name)
    with open(file_path, "wb") as f:                           #Opens the file in write-binary mode because pdfs are not just a text they contain fonts , sizes .. wb to preserve the structure
        f.write(file.getbuffer())

def create_vector_store(file_path):
    loader = PyPDFLoader(file_path)          #load pdf file
    documents = loader.load()                #extract text from pdf
    
    text_splitter =RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=300,
        add_start_index=True
    )                       #create chunks of 2000 characters with an overlap of 300 to maintain context

    chunked_docs = text_splitter.split_documents(documents)
    db = FAISS.from_documents(chunked_docs, embeddings)  #convert text into vector representations and store them in faiss vector db
    return db


def retrieve_docs(db, query, k=4):        #this methos searches for most relevent 4 chunks in our db  given the user's query
    print(db.similarity_search(query))
    return db.similarity_search(query, k)


def question_pdf(question, documents):
    context = "\n\n".join([doc.page_content for doc in documents]) # joins retrieved document chunks into a single text block.
    prompt = ChatPromptTemplate.from_template(template) #creates a structured prompt using the predefined template.
    chain = prompt | model 

    return chain.invoke({"question": question, "context": context})