import streamlit as st

# Set page config
st.set_page_config(page_title="AI Chat Models", page_icon="🤖", layout="wide")

# Title of the page
st.title('Welcome to the Chat App! 👋')

# Custom CSS for styling
st.markdown("""
    <style>
        .box {
            border: 1px solid #aaa;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            background-color: #f9f9f9;
        }
        .model-title {
            color: #ff4b4b;
            font-weight: bold;
            margin: 0;
        }
        .model-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-right: 10px;
        }
        .model-description {
            padding: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)

# Container for the AI models
with st.container():
    # Using columns to display the AI models side by side
    col1, col2, col3 = st.columns(3)
    
    # Google Gemini 1.5 Pro
    with col1:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown("#### 🌌 Google Gemini 1.5 Pro", unsafe_allow_html=True)
        st.write("""
            A versatile chatbot model powered by Vertex AI SDK, excelling in understanding context 
            and generating human-like responses across diverse topics.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # GPT-4
    with col2:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown("#### 🧠 GPT-4", unsafe_allow_html=True)
        st.write("""
            OpenAI's language model famous for its depth of knowledge, able to perform a wide 
            variety of tasks with nuance and understanding.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Claude 3 Opus
    with col3:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown("#### 🎶 Claude 3 Opus", unsafe_allow_html=True)
        st.write("""
            Built by Anthropic, Claude 3 Opus focuses on safe and ethically-aligned conversations, 
            providing accurate and considerate responses.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("👈 Select a chat app from the sidebar to start chatting! Explore different AI chat experiences here!")
