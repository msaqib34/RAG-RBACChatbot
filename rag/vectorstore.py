from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(docs):

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    
    return vectorstore