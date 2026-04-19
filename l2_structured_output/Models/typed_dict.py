from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from Schemas.review import Review

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=2)
structured_model=model.with_structured_output(Review)

# Positive Review
res1=structured_model.invoke("The experience was excellent. The service was fast, the staff was friendly, and everything was well organized. I would definitely recommend it and use it again.")

# Neutral Review
res2=structured_model.invoke("The experience was okay. The service worked as expected, but nothing stood out. There were a few minor delays, but overall it was acceptable.")

# Negative Review
res3=structured_model.invoke("The experience was disappointing. The service was slow, and the staff was not very helpful. It did not meet expectations, and I would not recommend it.")

print(res1)
print(res2)
print(res3)