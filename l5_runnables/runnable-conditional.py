from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a report on the following {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Summarize The Follwoing Text {text}",
    input_variables=["text"]
)


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()


report_gen=RunnableSequence(prompt1,model,parser)
conditional_chain=RunnableBranch(
    (lambda x:len(x.split())>300, RunnableSequence(prompt2,model,parser)),
     RunnablePassthrough()
)

chain=report_gen| conditional_chain
res=chain.invoke({"topic":"Machine Learning"})