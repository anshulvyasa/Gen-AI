from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()
    
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["P","O","N"] = Field(description="P Represent positive sentiment, O represent Neutral Sentiment and N represent negative sentiment")

parser2=PydanticOutputParser(pydantic_object=Feedback)    

prompt1=PromptTemplate(
    template="What is the Feedback Sentiment {format_instruction} {feedback}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain= prompt1 | model | parser2

prompt2=PromptTemplate(
    template="Generate me Response for The following Feedback \n {feedback} P is Positive",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Generate me Response for The Following Negative Sentiment \n {feedback} N is Negative",
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x: x.sentiment=='P', prompt2 | model | parser),
    (lambda x: x.sentiment=='N', prompt3 | model | parser),
    RunnableLambda(lambda x: "Coundn't Find Sentiment")
)

chain= classifier_chain | branch_chain

print(chain.invoke({'feedback':"Such a Bad Product don't ever use it"}))


