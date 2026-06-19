from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_db():

    docs = []

    pdf_files = [
        "docs/faq.pdf",
        "docs/password_reset.pdf",
        "docs/billing_policy.pdf"
    ]

    for file in pdf_files:
        loader = PyPDFLoader(file)
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)

    db.save_local("vectorstore")

    return db
