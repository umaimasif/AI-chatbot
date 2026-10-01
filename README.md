# AI Chatbot

A simple command-line AI chatbot built with Python and the Groq API.

The chatbot accepts messages from the user, sends them to a large language model through the Groq API, receives the generated response, and displays it in the terminal.

## Features

* AI-powered conversations
* Groq API integration
* Llama language model
* Conversation history
* System prompt
* Error handling
* Environment variable for API key
* Simple command-line interface

## Technologies Used

* Python
* Groq API
* Groq Python SDK
* python-dotenv
* Llama 3.3 70B model

## Project Structure

```text
AI-Chatbot/
│
├── chatbot.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

The chatbot follows this basic flow:

```text
User enters message
        ↓
Python application
        ↓
Conversation history
        ↓
Groq API
        ↓
Llama language model
        ↓
AI response
        ↓
Terminal
```

The application keeps the conversation history in a Python list called `messages`.

Each message has a role:

* `system` — defines the assistant's behavior
* `user` — contains the user's message
* `assistant` — contains the AI's response

This allows the model to receive previous messages along with the latest user input.

## API Integration

The project uses the Groq Python SDK.

The API client is created using the API key stored in the `.env` file.

The API request sends the conversation history to the selected model and receives the generated response.

Example:

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=0.7
)
```

The response is then extracted and displayed to the user.

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project directory

```bash
cd AI-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create the `.env` file

Create a file named `.env` and add:

```env
GROQ_API_KEY=your_groq_api_key
```

### 7. Run the chatbot

```bash
python chatbot.py
```

## Example

```text
==================================================
              AI CHATBOT
==================================================
Powered by Groq + Llama
Type 'exit' to quit.
==================================================

You: What is artificial intelligence?

AI: Artificial intelligence is a field of computer science
that focuses on creating systems that can perform tasks
that normally require human intelligence.

You: What are some examples?

AI: Some examples include recommendation systems,
computer vision, speech recognition, and generative AI.

You: exit

AI: Goodbye! Have a great day.
```

## What I Learned

Through this project, I learned:

* How to integrate an external AI API into a Python application
* How API keys should be stored securely using environment variables
* How chat completion APIs work
* How system, user, and assistant messages are structured
* How conversation history can be maintained
* How to handle API errors
* How to organize a small Python project
* How to prepare a project for GitHub

## What I Would Improve Next

If I continued developing this project, I would add:

* A web-based user interface
* Markdown rendering
* Streaming responses
* Better conversation management
* Chat history persistence
* Voice input and output
* Authentication
* Additional AI features

## Security

The API key is stored in `.env` and is excluded from Git using `.gitignore`.

The API key should never be committed to the GitHub repository.
