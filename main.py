from dotenv import load_dotenv                          # Dotenv for loading environment variables.
import os                                               # OS module for interacting with the operating system.
import streamlit as st                                  # Streamlit library for creating web apps.
from streamlit_chat import message as stchat_message    # Streamlit's chat UI component.

# Import chat-related modules from LangChain.
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()  # Load environment variables from a .env file.

    # Load the OpenAI API key from an environment variable.
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPEN_API_KEY") == "":
        print(">> OPENAI_API_KEY is not set")
        exit(1)
    else: 
        print(">> OPENAI_API_KEY is set")
    
    # Define Streamlit page configuration.
    st.set_page_config(
        page_title="Your own ChatGPT",  # Title of the page.
        page_icon="💬"                   # Icon of the page.
    )

def main():
    init()  # Call the initialization function.
    
    # Create an instance of ChatOpenAI from LangChain
    chat = ChatOpenAI(temperature=0.5)  # Temperature parameter determines the creativity of the conversation.
    
    # Initialize the Streamlit session state to keep track of the messages.
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Set up the header of the page.
    st.header("Your own ChatGPT 💬")
    
    # Create a text input field in the sidebar for user input.
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")
        show_message = st.radio(
            "Set a message visibility 👀",
            key="visibility",
            options=["visible", "hidden"],
            index=1,
        )
    
        role = st.radio(
            "Assign a role to the bot 🤖",
            key="role",
            options=["Assistant", "Counselor", "Teacher", "Artist"]
        )
    
    # Process the user's message.
    if user_input:
        # Assigning roles
        if role == "Assistant":
            st.session_state.messages.append(SystemMessage(content="You are a helpful assistant."))
        elif role == "Counselor":
            st.session_state.messages.append(SystemMessage(content="You are a counselor who provides effective solutions to user's problem with an empathetic tone."))
        elif role == "Teacher":
            st.session_state.messages.append(SystemMessage(content="You are an understanding teacher who explains concepts user asks about with easy explanations. If possible, give analogies or useful examples. "))
        elif role == "Artist":
            st.session_state.messages.append(SystemMessage(content="You are a creative artist who provides innovative and creative ideas."))
        st.session_state.messages.append(HumanMessage(content=user_input))  # Add the user's message to the session state.
        with st.spinner("Thinking..."):                                     # Show a spinner while waiting for a response.
            response = chat(st.session_state.messages)                      # Get a response from the LangChain chatbot.
        st.session_state.messages.append(AIMessage(content=response.content))  # Add the AI's response to the session state.

    # Iterate through the stored messages and display them on the screen.
    messages = st.session_state.get('messages', [])
    
    for i, msg in enumerate(messages):                              # Display all messages
        if i % 3 == 0:                                                          
            continue                                                           # Do not display system messages. 
        elif i % 3 == 1:
            stchat_message(msg.content, is_user=True, key=str(i) + '_user')    # Display user messages.
        else:
            stchat_message(msg.content, is_user=False, key=str(i) + '_ai')     # Display AI messages.

    if show_message == "visible":
        st.write(messages)

if __name__ == '__main__':
    main()