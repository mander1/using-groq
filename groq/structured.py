import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import dotenv
import instructor
dotenv.load_dotenv()

class Character(BaseModel):
    name: str
    fact: List[str] = Field(..., description="A list of facts about the subject")


client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

client = instructor.from_groq(client, mode=instructor.Mode.TOOLS)

resp = client.chat.completions.create(
    model="llama3-70b-8192",  # Updated to a currently supported model
    messages=[
        {
            "role": "user",
            "content": "Tell me about the company Tesla",
        }
    ],
    response_model=Character,
)
print(resp.model_dump_json(indent=2))