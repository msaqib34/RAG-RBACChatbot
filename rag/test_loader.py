
# from loader import load_csv_files   # adjust import if needed

# docs = load_csv_files("resources/data/hr")

# print("Docs loaded:", len(docs))

# for doc in docs:
#     print(doc.page_content[:100])  # preview first 100 chars

# from loader import load_md_files   # adjust import if needed
# docs = load_md_files("resources/data/engineering")

# print("Docs loaded:", len(docs))

# for doc in docs:
#     print(doc.page_content[:100])  # preview first 100 chars    



from loader import load_md_files ,load_all_data  # adjust import if needed
docs = load_all_data("resources/data/")

print("Docs loaded:", len(docs))

for doc in docs:
    print(doc.metadata)  # print metadata to verify role is included

    