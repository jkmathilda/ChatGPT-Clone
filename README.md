# Chatbot

Chatbots are one of the central LLM use-cases. The core features of chatbots are that they can have long-running conversations and have access to information that users want to know about.

Aside from basic prompting and LLMs, memory and retrieval are the core components of a chatbot. Memory allows a chatbot to remember past interactions, and retrieval provides a chatbot with up-to-date, domain-specific information.

![chat_use_case-eb8a4883931d726e9f23628a0d22e315](https://github.com/jkmathilda/ChatGPT-Chatbot/assets/142202145/9cf8af68-1851-410d-bae3-167039dbf35b)

# Getting Started

To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Cloning the Repository

    git clone https://github.com/jkmathilda/ChatGPT-Chatbot.git

### Setting up a Virtual Environment

    cd ./ChatGPT-Chatbot

    pyenv versions

    pyenv local 3.11.6

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore

    ls -la

    python -m venv .venv        # create a new virtual environment

    source .venv/bin/activate   # Activate the virtual environment

    python -V                   # Check a python version

### Install the required dependencies

    pip install -r requirements.txt

### Configure the Application

To configure the application, there are a few properties that can be set the environment

    echo 'OPENAI_API_KEY="sk-...."' >> .env

### Running the Application

    python -m streamlit run main.py

### Deactivate the virtual environment

    deactivate

# Example

![Image 2023-12-24 at 8 15 PM](https://github.com/jkmathilda/ChatGPT-Chatbot/assets/142202145/139d65b5-4694-4176-b3e2-047d7616a728)

# Reference

Chatbots (on LangChain)
[https://python.langchain.com/docs/use_cases/chatbots]

Youtube : Create a ChatGPT clone using Streamlit and LangChain
[https://www.youtube.com/watch?v=IaTiyQ2oYUQ]
