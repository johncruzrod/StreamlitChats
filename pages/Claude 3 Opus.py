import streamlit as st
from anthropic import Anthropic
import os

# Set up the Anthropic client
# Assuming you've set ANTHROPIC_API_KEY in your environment or .env file
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

st.set_page_config(layout="wide")
st.title('Chat with Claude')  # Simplified title

# Check if coming from a different app and reset chat
if 'last_app' not in st.session_state or st.session_state['last_app'] != 'claude':
    st.session_state['claude_messages'] = []
st.session_state['last_app'] = 'claude'

# Function to format and send messages to Claude API
def run_claude(messages, system_prompt):
    # Prepend the system prompt to the conversation
    messages = [{"role": "system", "content": system_prompt}] + messages

    response = client.messages.create(
        max_tokens=1024,
        messages=messages,
        model="claude-3-opus-20240229",
    )
    return response.content  # Extract assistant's response

# Define the hard-coded system prompt
system_prompt = "You are a helpful AI assistant. Provide clear and detailed answers to any user request, being helpul and informative."

# Handle chat input and display
if "claude_messages" not in st.session_state:
    st.session_state.claude_messages = []

# Chat history
for message in st.session_state.claude_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for new message
user_question = st.chat_input("What is up?")  # Using chat_input
if user_question:
    # Check if the last message in the chat history is from the user
    if not st.session_state.claude_messages or st.session_state.claude_messages[-1]["role"] == "assistant":
        st.session_state.claude_messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)
        with st.chat_message("assistant"):
            with st.spinner('Waiting for Claude to respond...'):
                response_content = run_claude(st.session_state.claude_messages, system_prompt)
                response_text = response_content[0].text  # Extract the text from the first content block
                st.markdown(response_text)
                st.session_state.claude_messages.append({"role": "assistant", "content": response_text})
    else:
        st.warning("Please wait for Claude's response before sending another message.")
