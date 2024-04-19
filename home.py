import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome to the AI Chat Models", page_icon="🤖", layout="wide")

# Header of the page
st.title('Welcome to the Chat App! 👋')

# Container and columns to create boxes around each model's description
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    # CSS to inject contained in a markdown
    st.markdown("""
        <style>
        .box {
            border: 2px solid #9baacf;
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
        }
        img {
            max-height: 150px;  /* Adjust if needed */
            margin: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    with col1:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.image("gemini.png", use_column_width=True, caption='Google Gemini 1.5 Pro')
        st.header("Google Gemini 1.5 Pro 🌌")
        st.write("""
            Google's Gemini 1.5 Pro is a cutting-edge chatbot model powered by Vertex AI SDK. 
            This model is exceptional at understanding context and generating human-like responses.
            It's versatile and can engage in a wide range of conversation topics.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.image("gpt4.png", use_column_width=True, caption='OpenAI GPT-4')
        st.header("GPT-4 🧠")
        st.write("""
            OpenAI's GPT-4 is a top-tier language model renowned for its extensive knowledge and comprehension.
            It's adept at performing a variety of tasks, including answering complex questions and creating content
            with depth and nuance.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.image("claude.png", use_column_width=True, caption='Claude 3 Opus')
        st.header("Claude 3 Opus 🎶")
        st.write("""
            Claude 3 Opus by Anthropic focuses on safety and ethical alignment in AI conversations.
            It ensures that responses are not only accurate but also respectful and considerate of the user's intentions.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("👈 Select a chat app from the sidebar to start chatting! Enjoy exploring different AI chat experiences here!")
