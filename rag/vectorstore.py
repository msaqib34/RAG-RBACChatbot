

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(
         collection_name="example_collection",
         embedding_function=embeddings,
        persist_directory="chroma_db",  # Where to save data locally, remove if not necessary
        )

    vector_store.add_documents(docs)
    return vector_store

