from rag.loader import load_all_data
from rag.splitter import split_docs

docs = load_all_data("resources/data")

print("Before splitting:", len(docs))

split_docs_list = split_docs(docs)

print("After splitting:", len(split_docs_list))

# Preview
for doc in split_docs_list[:2]:
    print("Content:", doc.page_content[:100])
    print("Metadata:", doc.metadata)
    print("------")