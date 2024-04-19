import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide")

# Header of the page
st.title('Welcome to the Chat App! 👋')

# Sidebar selection
app_choice = st.sidebar.radio("Choose your Chat App", ("Chat with Gemini 1.5 Pro", "Chat with GPT-4", "Chat with Claude 3 Opus"))

# Description based on the selection
if app_choice == "Chat with Gemini 1.5 Pro":
    app_description = """
    **Gemini 1.5 Pro** is Google's latest chatbot model powered by Vertex AI SDK. It excels in understanding and generating 
    human-like text based on the input provided. It's designed for versatility and can handle a broad range of conversation topics.
    """
elif app_choice == "Chat with GPT-4":
    app_description = """
    **GPT-4** by OpenAI is a state-of-the-art language model known for its depth and breadth of knowledge. 
    It can assist in various tasks, including answering questions, writing content, and more, providing
    informative and contextually relevant responses.
    """
elif app_choice == "Chat with Claude 3 Opus":
    app_description = """
    **Claude 3 Opus** is a powerful conversational AI developed by Anthropic. It focuses on safety and alignment 
    to provide responses that are not only accurate but also considerate and aligned with user intent.
    """

# Display the selected chat app description
st.markdown(app_description)

# Footer
st.markdown("""
    👈 Select a chat app from the sidebar to start chatting!
    Enjoy exploring different AI chat experiences here!
""")
