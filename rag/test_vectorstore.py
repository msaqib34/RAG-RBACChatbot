

from rag.vectorstore import create_vector_store
from rag.loader import load_all_data
from rag.splitter import split_docs

docs = load_all_data("resources/data")
split_docs_list = split_docs(docs)

print("Docs after split:", len(split_docs_list))
vector_store = create_vector_store(split_docs_list)

print("Vector store created with documents.")