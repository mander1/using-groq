from groq import Groq
import os
import dotenv
dotenv.load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
