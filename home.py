import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide")

# Custom CSS styles to adhere to your design
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
        height: 150px; /* Fixed height for all images */
        object-fit: contain; /* Keeps the aspect ratio of the image */
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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Welcome to the Chat App! 👋</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Choose an AI-powered chat app to start an engaging conversation:</div>', unsafe_allow_html=True)

# Create columns for the models
col1, col2, col3 = st.columns((1, 1, 1))

# Displaying images and model details
models = {
    "Gemini 1.5 Pro": "gemini.png",
    "GPT-4": "gpt4.png",
    "Claude 3 Opus": "claude.png"
}

for i, (model_name, image_path) in enumerate(models.items()):
    with (col1, col2, col3)[i]:
        st.markdown(f"<div class='model-card'>", unsafe_allow_html=True)
        st.image(image_path, width=200, caption=model_name)
        st.markdown(f"<div class='model-title'>{model_name}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='model-description'>A description specific to {model_name}.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="bottom-text">👈 Select a chat app from the sidebar to start chatting!</div>', unsafe_allow_html=True)
