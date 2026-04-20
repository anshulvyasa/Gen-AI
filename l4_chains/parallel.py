from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1=PromptTemplate(
    template="Generate me short and crisp notes on the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="generate me 5 questions quiz on the {topic}",
    input_variables=['topic']
)

prompt3=PromptTemplate(
    template="combine the notes and quiz in a single document Notes is -> {notes} Quiz is ->. {quiz}",
    input_variables=['notes','quiz']
)

model1=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
model2=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser=StrOutputParser()


parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain= prompt3 | model2 | parser

# Our Final Chain
chain= parallel_chain | merge_chain
 
res=chain.invoke({'topic':"democracy"})
print(res)