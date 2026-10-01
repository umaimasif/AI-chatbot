import os
from dotenv import load_dotenv
from groq import Groq



load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
   raise ValueError("GROQ_API_KEY is not set in the .env file")



client = Groq(api_key=os.environ["GROQ_API_KEY"])



messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]


print("AI Chatbot")
print("Type 'exit' to quit.")
print("-" * 40)


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

   
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )

        assistant_message = response.choices[0].message.content

       
        messages.append({
            "role": "assistant",
            "content": assistant_message
        })

        print(f"AI: {assistant_message}")

    except Exception as e:
        print(f"Error: {e}")
