from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
