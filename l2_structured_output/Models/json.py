import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

with open("Schemas/json_schema.json", "r") as f:
    schema = json.load(f)
    
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structed_model=model.with_structured_output(schema)

res=structed_model.invoke("Create a realistic student record with reasonable academic performance.")    
print(res)


