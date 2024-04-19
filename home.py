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
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    .intro {
        font-size: 24px;
        margin-bottom: 40px;
        text-align: center;
        color: #586069;
    }
    .model-card {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        padding: 20px;
        height: 100%;
        background-color: #fff;
        transition: all 0.3s ease;
    }
    .model-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
    }
    .model-image {
        display: block;
        width: 100%;
        max-width: 200px;
        margin: 0 auto;
        margin-bottom: 20px;
    }
    .model-title {
        font-size: 24px;
        font-weight: 600;
        color: #1f77b4;
        margin-bottom: 10px;
        text-align: center;
    }
    .model-description {
        font-size: 16px;
        color: #586069;
        text-align: center;
        margin-bottom: 0;
    }
    .bottom-text {
        font-size: 20px;
        margin-top: 40px;
        text-align: center;
        font-weight: bold;
        color: #2c3e50;
    }
    .sidebar .sidebar-content {
        background-color: #f6f8fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('<div class="title">Welcome to the Chat App! 👋</div>', unsafe_allow_html=True)

st.write('<div class="intro">Choose an AI-powered chat app to start an engaging conversation:</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 1, 1))

with col1:
    with st.container():
        st.markdown(
            """
            <div class="model-card">
                <img src="gemini.png" alt="Gemini 1.5 Pro" class="model-image">
                <h3 class="model-title">Gemini 1.5 Pro</h3>
                <p class="model-description">Powered by Vertex AI SDK and the Gemini model for engaging conversations.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container():
        st.markdown(
            """
            <div class="model-card">
                <img src="gpt4.png" alt="GPT-4" class="model-image">
                <h3 class="model-title">GPT-4</h3>
                <p class="model-description">Powered by OpenAI's GPT-4 model for advanced language understanding and generation.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

with col3:
    with st.container():
        st.markdown(
            """
            <div class="model-card">
                <img src="claude.png" alt="Claude 3 Opus" class="model-image">
                <h3 class="model-title">Claude 3 Opus</h3>
                <p class="model-description">Powered by Anthropic's Claude 3 Opus model for thoughtful and coherent responses.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.sidebar.title("Navigation")
app_selection = st.sidebar.radio("Select an app", ("Home", "Chat with Gemini 1.5 Pro", "Chat with GPT-4", "Chat with Claude 3 Opus"))

if app_selection != "Home":
    st.sidebar.success(f"You selected: {app_selection}")
else:
    st.write('<div class="bottom-text">👈 Select a chat app from the sidebar to start chatting!</div>', unsafe_allow_html=True)
