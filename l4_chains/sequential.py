from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template="Generate me a detialed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarize it in 5 points {topic}",
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2  | model | parser 

res=chain.invoke({'topic':"Unemployment in India"})
print(res)