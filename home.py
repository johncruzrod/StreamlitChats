import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋")

st.write("# Welcome to the Chat App! 👋")

st.sidebar.success("Select a chat app from the sidebar.")

st.markdown(
    """
    This is a multipage chat application built with Streamlit.
    You can choose between two chat apps:
    - Chat with Gemini: Powered by Vertex AI SDK and the Gemini model.
    - Chat with GPT-4: Powered by OpenAI's GPT-4 model.
    **👈 Select a chat app from the sidebar to start chatting!**
    """
)
