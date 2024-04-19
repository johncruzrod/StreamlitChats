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

# Handle chat input and display
if "claude_messages" not in st.session_state:
    st.session_state.claude_messages = []

user_input = st.text_input("What is up?", key="claude_input")
if st.button('Send', key='claude_send'):
    if user_input:
        st.session_state.claude_messages.append({"role": "user", "content": user_input})
        # Send message to Claude
        message = client.messages.create(
            max_tokens=1024,
            messages=st.session_state.claude_messages,
            model="claude-3-opus-20240229",
        )
        if message:
            assistant_response = message.content[-1] if message.content else "No response generated."
            st.session_state.claude_messages.append({"role": "assistant", "content": assistant_response})
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
