# Strategy:

# Try splitting by paragraphs
# If too big → split by lines
# Still big → split by words
# Last → characters

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader("documents/data.txt")
doc=loader.load()[0].page_content;

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks=splitter.split_text(doc)

print(len(chunks))
print(chunks)