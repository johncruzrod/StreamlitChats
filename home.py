import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome to the AI Chat Models", page_icon="🤖", layout="wide")

# Header of the page
st.title('Welcome to the Chat App! 👋')

# AI Model Information Section using a three-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Google Gemini 1.5 Pro 🌌")
    st.write("""
        Google's Gemini 1.5 Pro is a cutting-edge chatbot model powered by Vertex AI SDK. 
        This model is exceptional at understanding context and generating human-like responses.
        It's versatile and can engage in a wide range of conversation topics.
    """)

with col2:
    st.header("GPT-4 🧠")
    st.write("""
        OpenAI's GPT-4 is a top-tier language model renowned for its extensive knowledge and comprehension.
        It's adept at performing a variety of tasks, including answering complex questions and creating content
        with depth and nuance.
    """)

with col3:
    st.header("Claude 3 Opus 🎶")
    st.write("""
        Claude 3 Opus by Anthropic focuses on safety and ethical alignment in AI conversations.
        It ensures that responses are not only accurate but also respectful and considerate of the user's intentions.
    """)

# Footer
st.markdown("👈 Select a chat app from the sidebar to start chatting! Enjoy exploring different AI chat experiences here!")
