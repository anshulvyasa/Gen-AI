from Schemas.student import Student
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structed_model= model.with_structured_output(Student);

res=structed_model.invoke("Create a realistic student record with good academic performance")
print(res)