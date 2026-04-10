# New/Correct
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)

