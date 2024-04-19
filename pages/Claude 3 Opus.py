import streamlit as st
from anthropic import Anthropic
import os

# Set up the Anthropic client
# Assuming you've set ANTHROPIC_API_KEY in your environment or .env file
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

st.set_page_config(layout="wide")
st.title('Chat with Claude using Anthropic')

# Check if coming from a different app and reset chat
if 'last_app' not in st.session_state or st.session_state['last_app'] != 'claude':
    st.session_state['claude_messages'] = []
st.session_state['last_app'] = 'claude'

# Function to format and send messages to Claude API
def send_message_to_claude(conversation):
    response = client.messages.create(
        max_tokens=1024,
        messages=conversation,
        model="claude-3-opus-20240229",
    )
    return response

# Handle chat input and display
if "claude_messages" not in st.session_state:
    st.session_state.claude_messages = []

# Chat history
for message in st.session_state.claude_messages:
    with st.container():
        role = "user" if message["role"] == "user" else "assistant"
        st.chat_message(role, message["content"])

# Input for new message
user_input = st.text_input("What is up?", key="claude_input")
if st.button('Send', key='claude_send'):
    if user_input:
        st.session_state.claude_messages.append({"role": "user", "content": user_input})
        response = send_message_to_claude(st.session_state.claude_messages)
        if response and 'messages' in response:
            # Extract the assistant's response from the last message
            assistant_response = response['messages'][-1]['content']
            
            # Append the assistant's response to the chat history
            st.session_state.claude_messages.append({"role": "assistant", "content": assistant_response})
            
            # Display the assistant's response in the chat
            with st.container():
                st.chat_message("assistant", assistant_response)
        else:
            st.error("Error occurred while communicating with Claude API.")
