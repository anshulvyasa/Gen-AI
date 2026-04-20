from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1=PromptTemplate(template="Write a Tweet For me on the following topic \n {topic}",input_variables=["topic"])
prompt2=PromptTemplate(template="Write a jLindlen description for my post for the following Topic /n {topic}",input_variables=["topic"])

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser=StrOutputParser()


parallen_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedn': RunnableSequence(prompt2,model,parser)
})

res=parallen_chain.invoke({'topic':"I got 2 month intenship at Accenture"})
print(res)

