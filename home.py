import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide")

# Custom CSS styles
st.markdown("""
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
            background-color: #fff;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .model-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
        }
        .model-image {
            max-height: 150px; /* Fixed height for all images */
            object-fit: contain; /* Keeps the aspect ratio of the image */
            width: auto; /* Adjusts the width automatically */
        }
        .model-title {
            font-size: 24px;
            font-weight: 600;
            color: #1f77b4;
            margin-top: 20px;
            text-align: center;
        }
        .model-description {
            font-size: 16px;
            color: #586069;
            text-align: center;
            margin-top: 20px;
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

st.markdown('<div class="title">Welcome to the Chat App! 👋</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Choose an AI-powered chat app to start an engaging conversation:</div>', unsafe_allow_html=True)

# Displaying images and model details in a card layout
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='model-card'>", unsafe_allow_html=True)
        st.image("gemini.png", use_column_width=True, caption="Gemini 1.5 Pro", output_format="PNG")
        st.markdown("<div class='model-title'>Gemini 1.5 Pro</div>", unsafe_allow_html=True)
        st.markdown("<div class='model-description'>Powered by Vertex AI SDK and the Gemini model for engaging conversations.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='model-card'>", unsafe_allow_html=True)
        st.image("gpt4.png", use_column_width=True, caption="GPT-4", output_format="PNG")
        st.markdown("<div class='model-title'>GPT-4</div>", unsafe_allow_html=True)
        st.markdown("<div class='model-description'>Powered by OpenAI's GPT-4 model for advanced language understanding and generation.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='model-card'>", unsafe_allow_html=True)
        st.image("claude.png", use_column_width=True, caption="Claude 3 Opus", output_format="PNG")
        st.markdown("<div class='model-title'>Claude 3 Opus</div>", unsafe_allow_html=True)
        st.markdown("<div class='model-description'>Powered by Anthropic's Claude 3 Opus model for thoughtful and coherent responses.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="bottom-text">👈 Select a chat app from the sidebar to start chatting!</div>', unsafe_allow_html=True)
