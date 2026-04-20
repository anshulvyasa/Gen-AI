from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt=PromptTemplate(template="Write a joke about the following topic {topic}",input_variables=["topic"])
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)
res=chain.invoke({"topic":"College"})

print(res)

