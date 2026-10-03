import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add your API key to the .env file."
    )

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are a helpful AI assistant for students and developers.

Your responsibilities:
- Give clear and accurate answers.
- Explain technical concepts in simple language.
- Provide examples when useful.
- If you are unsure about something, say so instead of inventing information.
- Keep responses reasonably concise unless the user asks for detail.
"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

def clear_chat():
    global messages

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("\nChat history cleared.\n")
def get_ai_response(user_message):

    messages.append({
        "role": "user",
        "content": user_message
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

        return assistant_message

    except Exception as error:

        messages.pop()

        print(f"\nError communicating with AI: {error}\n")

        return None

def main():

    print("=" * 60)
    print("                 AI CHATBOT")
    print("=" * 60)

    print("Powered by Groq + Llama")
    print()
    print("Commands:")
    print("  exit  → Quit chatbot")
    print("  clear → Clear conversation history")
    print("=" * 60)

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Please enter a message.")
            continue
        if user_input.lower() == "exit":

            print("\nAI: Goodbye! Have a great day.")
            break
        if user_input.lower() == "clear":

            clear_chat()
            continue

        print("\nAI: Thinking...")

        response = get_ai_response(user_input)

        if response:
            print(f"\nAI: {response}")

if __name__ == "__main__":
    main()
