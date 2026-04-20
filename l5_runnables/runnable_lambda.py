from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

prompt=PromptTemplate(
    template="Generate me Joke on The Following Topic don't give me option just give me one clear,crisp and short joke{topic}",
    input_variables=["topic"]
)


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()


joke_chain=RunnableSequence(prompt,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'joke_word_count': RunnableLambda(lambda x:len(x.split()))
})

chain=RunnableSequence(joke_chain,parallel_chain)

res=chain.invoke({"topic":"Library"})
print("Joke is ",res["joke"])
print("Word Count is ",res["joke_word_count"])

