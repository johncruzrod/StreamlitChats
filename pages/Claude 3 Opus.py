import streamlit as st
import requests
import json

# Set wide layout for the Streamlit app
st.set_page_config(layout="wide")

# Streamlit UI setup
st.title('Chat with Claude 3 Opus')

# Check if coming from a different app and reset chat
if 'last_app' not in st.session_state or st.session_state['last_app'] != 'claude':
    st.session_state['claude_messages'] = []
st.session_state['last_app'] = 'claude'

# Function to send messages to Anthropic's Claude API
def send_message_to_claude(messages):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {st.secrets['anthropic_api_token']}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1024,
        "messages": messages
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API request failed", "status_code": response.status_code}

# Handle chat input and display
if "claude_messages" not in st.session_state:
    st.session_state.claude_messages = []

user_input = st.text_input("What is up?", key="claude_input")
if st.button('Send', key='claude_send'):
    if user_input:
        # Append user message
        st.session_state.claude_messages.append({"role": "user", "content": user_input})
        # Send message to Claude
        response = send_message_to_claude(st.session_state.claude_messages)
        if "error" not in response:
            # Display response from Claude
            assistant_message = response['messages'][-1]['content']
            st.session_state.claude_messages.append({"role": "assistant", "content": assistant_message})
            st.chat_message("assistant", assistant_message)
        else:
            st.error(f"Error: {response['error']} - Status Code: {response['status_code']}")
