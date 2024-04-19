import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome to the AI Chat Models", page_icon="🤖", layout="wide")

# Header of the page
st.title('Welcome to the Chat App! 👋')

# Use container and columns to create boxes around each model's description
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

    # CSS to inject contained in a markdown
    st.markdown("""
        <style>
        .box {
            border: 2px solid #9baacf;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .image-container img {
            max-width: 100%;
            max-height: 150px;  /* Adjust if needed */
        }
        </style>
        """, unsafe_allow_html=True)

    with col1:
        st.markdown("<div class='box'><div class='image-container'>", unsafe_allow_html=True)
        st.image("gemini.png", caption='Google Gemini 1.5 Pro')
        st.markdown("</div>", unsafe_allow_html=True) # Closing the image-container div
        st.write("""
            Google's Gemini 1.5 Pro is a cutting-edge chatbot model powered by Vertex AI SDK. 
            This model is exceptional at understanding context and generating human-like responses.
            It's versatile and can engage in a wide range of conversation topics.
        """)
        st.markdown("</div>", unsafe_allow_html=True) # Closing the box div

    with col2:
        st.markdown("<div class='box'><div class='image-container'>", unsafe_allow_html=True)
        st.image("gpt4.png", caption='OpenAI GPT-4')
        st.markdown("</div>", unsafe_allow_html=True) # Closing the image-container div
        st.write("""
            OpenAI's GPT-4 is a top-tier language model renowned for its extensive knowledge and comprehension.
            It's adept at performing a variety of tasks, including answering complex questions and creating content
            with depth and nuance.
        """)
        st.markdown("</div>", unsafe_allow_html=True) # Closing the box div

    with col3:
        st.markdown("<div class='box'><div class='image-container'>", unsafe_allow_html=True)
        st.image("claude.png", caption='Claude 3 Opus')
        st.markdown("</div>", unsafe_allow_html=True) # Closing the image-container div
        st.write("""
            Claude 3 Opus by Anthropic focuses on safety and ethical alignment in AI conversations.
            It ensures that responses are not only accurate but also respectful and considerate of the user's intentions.
        """)
        st.markdown("</div>", unsafe_allow_html=True) # Closing the box div

# Footer
st.markdown("👈 Select a chat app from the sidebar to start chatting! Enjoy exploring different AI chat experiences here!")
