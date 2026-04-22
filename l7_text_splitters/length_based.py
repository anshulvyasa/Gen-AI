from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader,PyPDFLoader

loader=TextLoader("documents/data.txt")
document=loader.load()[0].page_content

pdf_loader=PyPDFLoader("documents/anshul_lab7.pdf")


text_splitter = CharacterTextSplitter(
    chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(document)

pdf_parts=text_splitter.split_documents(pdf_loader.load())


for text in pdf_parts:
    print(text,end="\n \n")
print("**********************************************************************************************")

for text in texts:
    print(text,end="\n \n")