from langchain_community.document_loaders import PyMuPDFLoader
loader=PyMuPDFLoader("DM_Lab8_anshul.pdf")

res=loader.load()
print(res)