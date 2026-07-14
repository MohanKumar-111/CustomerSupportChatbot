import json
from openai import OpenAI
from groq import Groq

# Add your API keys
openai_client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
groq_client = Groq(api_key="YOUR_GROQ_API_KEY")

history = []

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    history.append({"role": "user", "content": query})

    try:
        # Try OpenAI first
        response = openai_client.responses.create(
            model="gpt-4.1-mini",
            input=history
        )

        answer = response.output_text
        print("\nOpenAI:", answer)

    except Exception:
        # Fallback to Groq
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=history
        )

        answer = response.choices[0].message.content
        print("\nGroq:", answer)

    history.append({"role": "assistant", "content": answer})

    # Save chat history
    with open("chat_history.json", "w") as file:
        json.dump(history, file, indent=4)
