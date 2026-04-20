from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path="directory",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

res=loader.load()
print(len(res))