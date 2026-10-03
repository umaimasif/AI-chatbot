# AI Chatbot 

A simple AI chatbot built with **Python** and the **Groq API**. The chatbot accepts user messages, sends them to an AI model, and displays the generated response in the terminal.

The project was developed as part of an AI internship practical task and was progressively improved with conversation history, a system prompt, input validation, loading feedback, error handling, and a clear-chat feature.

---

## Features

* 💬 Chat with an AI assistant through the terminal
* 🤖 Uses the Groq API for AI responses
* 🧠 Maintains conversation history during the session
* 📝 Uses a custom system prompt to define the assistant's behavior
* ⏳ Shows a loading message while waiting for the AI response
* 🧹 Clear conversation history with the `clear` command
* 🚪 Exit the chatbot with the `exit` command
* ⚠️ Handles API and other runtime errors
* ✅ Validates empty user input
* 🔐 Keeps the API key in a `.env` file instead of hard-coding it
* 📦 Simple project structure with minimal dependencies

---

## Technologies Used

* **Python**
* **Groq API**
* **Groq Python SDK**
* **python-dotenv**
* **Llama model**

---

## Project Structure

```text
AI-Chatbot/
│
├── chatbot.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### File Description

| File               | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| `chatbot.py`       | Main chatbot application                                 |
| `requirements.txt` | Python dependencies                                      |
| `.env`             | Stores the Groq API key                                  |
| `.gitignore`       | Prevents sensitive/unnecessary files from being uploaded |
| `README.md`        | Project documentation                                    |

---

## How the Chatbot Works

The basic flow of the application is:

```text
User
  ↓
Enter message
  ↓
Input validation
  ↓
Conversation history
  ↓
Groq API
  ↓
AI model
  ↓
AI response
  ↓
Display response
  ↓
Save response to conversation history
```

The chatbot keeps the previous messages in memory during the current session. This allows the AI to understand the context of previous messages.

---

## System Prompt

The chatbot uses a system prompt to define the role and behavior of the AI assistant.

The assistant is instructed to:

* Give clear and accurate answers
* Explain technical concepts in simple language
* Provide examples when useful
* Avoid making up information when uncertain
* Keep responses reasonably concise unless the user asks for more detail

This helps make the chatbot's behavior more consistent.

---

## Conversation History

The chatbot stores messages in a Python list called `messages`.

The conversation contains three types of messages:

```text
system
user
assistant
```

For example:

```python
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]
```

When the user sends a message, it is added to the list:

```python
messages.append({
    "role": "user",
    "content": user_message
})
```

After receiving the AI response, the response is also stored:

```python
messages.append({
    "role": "assistant",
    "content": assistant_message
})
```

The complete conversation history is then sent to the AI model with each request.

---

## Commands

The chatbot supports the following commands:

### `exit`

Closes the chatbot.

Example:

```text
You: exit

AI: Goodbye! Have a great day.
```

### `clear`

Clears the current conversation history and starts a new conversation.

Example:

```text
You: clear

Chat history cleared.
```

---

## Requirements

Before running the project, make sure you have:

* Python 3.10 or newer
* A Groq API key
* Internet connection

---

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then move into the project folder:

```bash
cd AI-Chatbot
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a file named:

```text
.env
```

inside the project folder.

Add your Groq API key:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
```

Replace `YOUR_GROQ_API_KEY_HERE` with your actual API key.

**Never upload your actual API key to GitHub.**

The `.env` file should be included in `.gitignore`.

---

## Run the Application

After activating the virtual environment and adding your API key, run:

```bash
python chatbot.py
```

You should see something similar to:

```text
============================================================
                 AI CHATBOT
============================================================
Powered by Groq + Llama

Commands:
  exit  → Quit chatbot
  clear → Clear conversation history
============================================================

You:
```

You can then start chatting with the AI.

---

## Example

```text
You: What is Python?

AI: Python is a high-level programming language known for
its simple syntax and wide range of applications.

You: What can I build with it?

AI: You can use Python to build web applications, AI systems,
automation scripts, data analysis tools, APIs, and more.
```

The second question can use the context of the previous conversation because conversation history is maintained.

---

## Error Handling

The application includes error handling around the API request.

If the API request fails, the chatbot displays an error message instead of crashing immediately.

Example:

```text
Error communicating with AI: ...
```

The user's failed message is also removed from the conversation history so that an unsuccessful request does not remain as part of the conversation.

---

## Input Validation

The chatbot checks whether the user entered an empty message.

For example:

```text
You:

Please enter a message.
```

This prevents unnecessary API requests when no message has been entered.

---

## Loading State

Before waiting for the API response, the chatbot displays:

```text
AI: Thinking...
```

This gives the user feedback that the application is processing the request.

---

## Security

The API key is stored in an environment file instead of directly inside the Python source code.

The `.gitignore` file contains:

```text
.env
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
```

This helps prevent sensitive information and unnecessary files from being committed to GitHub.

**Important:** Never commit your real API key to a public GitHub repository.

---

## What I Learned

Through this project, I learned how to:

* Work with an external AI API
* Use the Groq Python SDK
* Store and load environment variables using `python-dotenv`
* Send messages to an AI model
* Handle API responses
* Maintain conversation history
* Use system prompts to control AI behavior
* Implement input validation
* Implement error handling
* Provide loading feedback to users
* Structure a small Python AI application
* Use `.gitignore` to protect API credentials
* Prepare a project for GitHub submission

---

## Challenges and Solutions

### 1. Managing the API Key

**Challenge:**
The API key should not be written directly inside the source code.

**Solution:**
I used a `.env` file and loaded the API key with `python-dotenv`.

---

### 2. Maintaining Conversation Context

**Challenge:**
A chatbot should be able to understand previous messages during the same conversation.

**Solution:**
I stored system, user, and assistant messages in a `messages` list and sent the conversation history with each API request.

---

### 3. Handling API Errors

**Challenge:**
An API request can fail because of network problems, invalid credentials, rate limits, or other issues.

**Solution:**
I added `try/except` error handling around the API request and display an error message to the user.

---

### 4. Clearing Conversation History

**Challenge:**
Users may want to start a completely new conversation without restarting the program.

**Solution:**
I added a `clear` command that resets the `messages` list while keeping the system prompt.

---

## Improvements Added During Day 2 and Day 3

### Day 2 Improvements

* Proper Groq API integration
* System prompt
* Loading state
* Error handling
* Input validation
* Clean terminal interface

### Day 3 Improvements

* Conversation history
* Clear conversation command
* Improved system prompt
* Better user interaction
* Improved error handling
* More organized chatbot flow

---

## Future Improvements

Possible future improvements include:

* Web-based user interface
* Markdown rendering
* Persistent conversation history
* Multiple conversations
* Voice input and output
* Streaming AI responses
* Authentication
* Database storage
* Chat export functionality

These features were not required for the current internship task, so the project intentionally keeps the implementation simple.

---

## Architecture

The application follows a simple architecture:

```text
┌─────────────────┐
│      User       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Input Handler  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Conversation    │
│    History      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Groq API     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    AI Model     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   AI Response   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Terminal Output │
└─────────────────┘
```

---

## Testing

The chatbot was tested with:

* Normal questions
* Follow-up questions
* Multiple messages
* Empty input
* `clear` command
* `exit` command
* API error scenarios

---

## Conclusion

This project demonstrates a basic but functional AI chatbot using Python and the Groq API.

The project focuses on understanding the fundamental workflow of an AI application:

```text
User Input
    ↓
API Request
    ↓
AI Model
    ↓
AI Response
    ↓
User
```

It was then extended with conversation history, system instructions, validation, loading feedback, error handling, and chat controls.

The implementation intentionally remains simple so that the core AI API integration and chatbot logic are easy to understand and explain.

---

## Author

Umaima Asif

AI / Machine Learning Student


