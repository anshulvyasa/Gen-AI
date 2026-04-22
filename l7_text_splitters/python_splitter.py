# This Will Split The Python code into chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import TextLoader


loader=TextLoader("length_based.py")
docs=loader.load()[0].page_content
# print(loader.load()[0].page_content)

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks=splitter.split_text(docs)

print(len(chunks))
print(chunks[0])