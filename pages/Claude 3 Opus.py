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

# Display previous messages
for message in st.session_state.claude_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("What is up?", key="claude_input")
if st.button('Send', key='claude_send'):
    if user_input:
        # Append user message
        st.session_state.claude_messages.append({"role": "user", "content": user_input})
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        # Send message to Claude
        with st.spinner('Waiting for the assistant to respond...'):
            message = client.messages.create(
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": user_input}
                ] + [
                    {"role": "assistant", "content": m["content"]}
                    for m in st.session_state.claude_messages if m["role"] == "assistant"
                ],
                model="claude-3-opus-20240229",
            )
            if 'error' not in message:
                assistant_response = message.content[0]['text']  # Assuming the API returns a list with a single dict containing the text
                st.session_state.claude_messages.append({"role": "assistant", "content": assistant_response})
                # Display assistant message
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)
            else:
                st.error("An error occurred while fetching the response.")
        
        # Clear input box after sending the message
        st.session_state['claude_input'] = ""
