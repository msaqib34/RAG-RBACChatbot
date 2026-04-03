## Indexing logic For RAG
"""Data Indexing Process:

Data Loading: This involves importing all the documents or information to be utilized.

Data Splitting: Large documents are divided into smaller pieces, for instance, 
sections of no more than 500 characters each.

Data Embedding: The data is converted into vector form using an embedding model,
making it understandable for computers.

Data Storing: These vector embeddings are saved in a vector database, 
allowing them to be easily searched."""
# 1. User sends a message to /chat with their role
# 2. Based on the role, we determine which documents they have access to
# 3. We then use the message to retrieve relevant documents from that subset
# 4. Finally, we combine those documents into a response and return it to the user  

from langchain_community.document_loaders import TextLoader, CSVLoader

import os

# This function loads all .md files from a specified folder and returns them as documents

def load_md_files(folder_path):
    docs = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".md"):
            loader = TextLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())
    
    return docs


# LOAD CSV FILES (if needed, not used in current test)

def load_csv_files(folder_path):
    docs = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            loader = CSVLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())
    
    return docs    


# 🔥 MAIN FUNCTION (ADD ROLE HERE)
def load_all_data(base_path):

    all_docs = []

    for role in ["engineering", "marketing", "finance", "hr"]:

        role_path = os.path.join(base_path, role)

        docs = []
        docs += load_md_files(role_path)
        docs += load_csv_files(role_path)

        # 🔥 ADD ROLE METADATA HERE
        for doc in docs:
            doc.metadata["role"] = role

        all_docs.extend(docs)

    return all_docs