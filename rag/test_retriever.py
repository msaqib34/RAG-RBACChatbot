from rag.retriever import retrieve_with_rbac

docs = retrieve_with_rbac("What is data protection?", "engineering")

print("\n🔍 RESULTS:\n")

if not docs:
    print("❌ No documents retrieved")
else:
    for i, d in enumerate(docs):
        print(f"Doc {i+1}:")
        print("Content:", d.page_content[:200])
        print("Metadata:", d.metadata)
        print("------")