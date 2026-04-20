from langchain_community.document_loaders import TextLoader

loader=TextLoader('document.txt',encoding="utf-8")
print(loader.load())