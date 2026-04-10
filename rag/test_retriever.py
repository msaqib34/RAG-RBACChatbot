from rag.retriever import retrieve_with_rbac

docs = retrieve_with_rbac("What is data protection?", "engineering")

combined = "\n\n".join([d.page_content for d in docs])

print(combined)