# Runnable Passthrough produce same output as input

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1=PromptTemplate(
    template="Generate me Joke on The Following Topic don't give me option just give me one clear,crisp and short joke{topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate me joke Explanation of the Following Joke onlyu one explanation \n {joke}",
    input_variables=["joke"]
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser=StrOutputParser()


joke_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'joke_explanation': RunnableSequence(prompt2,model,parser)
})

chain=joke_chain | parallel_chain

res=chain.invoke({"topic":"College"})
print(res["joke"])
print(res["joke_explanation"])