import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide")

# Custom CSS styles
st.markdown(
    """
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 30px;
        text-align: center;
    }
    .intro {
        font-size: 24px;
        margin-bottom: 40px;
        text-align: center;
    }
    .model-title {
        font-size: 24px;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 10px;
        text-align: center;
    }
    .model-description {
        font-size: 18px;
        margin-bottom: 20px;
        text-align: justify;
    }
    .css-1q8dd3e {
        font-size: 18px;
        color: #2ca02c;
        font-weight: bold;
    }
    .container {
        padding: 20px;
        background-color: #f5f5f5;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 150px;
        margin-bottom: 20px;
    }
    .image-container img {
        max-height: 100%;
        max-width: 100%;
        object-fit: contain;
    }
    .bottom-text {
        font-size: 20px;
        margin-top: 40px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('<div class="title">Welcome to the Chat App! 👋</div>', unsafe_allow_html=True)

st.write('<div class="intro">This is a multipage chat application built with Streamlit. You can choose between three chat apps powered by different AI models:</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 1, 1))

with col1:
    with st.container():
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("gemini.png")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="model-title">Chat with Gemini 1.5 Pro</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="model-description">
            Powered by Vertex AI SDK and the Gemini model, this chat app utilizes Google's state-of-the-art Gemini 1.5 Pro model for engaging conversations. Gemini 1.5 Pro is known for its high-quality responses and ability to maintain context throughout the chat.
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container():
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("gpt4.png")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="model-title">Chat with GPT-4</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="model-description">
            Powered by OpenAI's GPT-4 model, this chat app leverages the advanced language understanding and generation capabilities of GPT-4. GPT-4 is renowned for its ability to engage in human-like conversations, provide informative responses, and assist with a wide range of tasks.
            </div>
            """,
            unsafe_allow_html=True
        )

with col3:
    with st.container():
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("claude.png")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="model-title">Chat with Claude 3 Opus</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="model-description">
            Powered by Anthropic's Claude 3 Opus model, this chat app offers an interactive experience with Claude, an AI assistant trained using constitutional AI principles. Claude 3 Opus excels at providing thoughtful and coherent responses while adhering to ethical guidelines.
            </div>
            """,
            unsafe_allow_html=True
        )

st.sidebar.success('Select a chat app from the sidebar.')

st.write('<div class="bottom-text">👈 Select a chat app from the sidebar to start chatting!</div>', unsafe_allow_html=True)
