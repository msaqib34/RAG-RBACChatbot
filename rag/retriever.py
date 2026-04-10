from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# 🔹 Load existing vector DB
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return vectorstore


# 🔥 MAIN FUNCTION (RBAC Retrieval)

def retrieve_with_rbac(query, role):

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 10,
            "filter": {"role": role}   # ✅ IMPORTANT FIX
        }
    )

    docs = retriever.invoke(query)


    

    return docs

# def retrieve_with_rbac(query, role):

#     vectorstore = load_vectorstore()

#     retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

#     docs = retriever.invoke(query)

#     print("\n🔍 RAW RESULTS (before filtering):\n")

#     for d in docs:
#         print(d.metadata)

#     return docs