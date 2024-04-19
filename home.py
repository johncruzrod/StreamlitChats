import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide")

# Custom CSS styles
st.markdown(
    """
    <style>
    .title {
        /* styles omitted for brevity */
    }
    .intro {
        /* styles omitted for brevity */
    }
    .model-card {
        /* styles omitted for brevity */
    }
    .model-card:hover {
        /* styles omitted for brevity */
    }
    .model-image {
        /* styles omitted for brevity */
    }
    .model-title {
        /* styles omitted for brevity */
    }
    .model-description {
        /* styles omitted for brevity */
    }
    .bottom-text {
        /* styles omitted for brevity */
    }
    .sidebar .sidebar-content {
        /* styles omitted for brevity */
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
        st.image(image_path, width=200, caption=model_name, output_format="PNG")
        st.markdown(f"""
            <h3 class='model-title'>{model_name}</h3>
            <p class='model-description'>A description specific to {model_name}.</p>
        </div>
        """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
app_selection = st.sidebar.radio("Select an app", ["Home"] + list(models.keys()))

if app_selection != "Home":
    st.sidebar.success(f"You selected: {app_selection}")
else:
    st.markdown('<div class="bottom-text">👈 Select a chat app from the sidebar to start chatting!</div>', unsafe_allow_html=True)
