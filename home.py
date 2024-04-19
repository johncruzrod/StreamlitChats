import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Chat Explorer",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown(
    """
<style>
/* General page styling */
body {
    font-family: 'Arial', sans-serif;
}

/* Title container */
.title-container {
    text-align: center;
    padding: 30px 20px;
    background-color: #f0f0f5; /* Light gray background */
    border-radius: 10px;
    margin-bottom: 20px;
}

/* Model card styling */
.model-card {
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 25px;
    margin: 15px;
    box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease; /* Add transition effects */
}

.model-card:hover {
    transform: translateY(-5px);  /* Slight upward movement on hover */
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2); /* More pronounced shadow on hover */
}

.model-image {
    max-width: 150px;
    margin: 0 auto 20px auto; /* Center image and add space below */
}

.model-name {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.model-description {
    color: #333;
}

/* Chatbot section */
.chatbot-section {
    text-align: center;
    padding: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)

# Title and introduction
st.markdown("<div class='title-container'>", unsafe_allow_html=True)
st.title("💬 AI Chat Explorer")
st.write("## Dive into the World of Conversational AI")
st.markdown("</div>", unsafe_allow_html=True)

# Model cards in columns
col1, col2, col3 = st.columns(3, gap="large")  # Add spacing between columns

with col1:
    with st.container():
        st.markdown("<div class='model-card'>", unsafe_allow_html=True)
        st.image("gemini.png", width=150, className="model-image")
        st.markdown("<div class='model-name'>Gemini 1.5 Pro</div>", unsafe_allow_html=True)
        st.caption("Vertex AI")
        st.write(
            "Google's powerful language model for understanding, responding, generating, and translating."
        )
        st.markdown("</div>", unsafe_allow_html=True)

# ... (Similar structure for col2 and col3 with GPT-4 and Claude images and descriptions)

# Chatbot section
st.markdown("<div class='chatbot-section'>", unsafe_allow_html=True)
st.write("## Engage in Conversation")
# TODO: Add your chatbot implementation here
st.markdown("</div>", unsafe_allow_html=True)

# Footer (optional)
# ...
