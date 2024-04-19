import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Chat Explorer",
    page_icon="🤖",
    layout="wide"
)

# Welcome message
st.title("🤖 AI Chat Explorer")
st.write("## Engage with Cutting-Edge Language Models!")

# Define CSS styles for containers with enhancements
container_styles = """
<style>
.model-container {
    background-color: #f0f0f5;
    border: 1px solid #ddd; 
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;  
}
.model-container:hover {
    background-color: #e8e8f0; 
}
</style>
"""

# Inject CSS styles
st.markdown(container_styles, unsafe_allow_html=True)

# Model descriptions with columns, containers, and images
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("<div class='model-container'>", unsafe_allow_html=True)
        st.image("gemini.png", width=200)
        st.subheader("Gemini 1.5 Pro (Vertex AI)")
        st.write("Google's advanced language model, trained on a massive dataset, excels in understanding and responding to complex queries, generating different creative text formats, and translating languages.")
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown("<div class='model-container'>", unsafe_allow_html=True)
        st.image("gpt4.png", width=200)
        st.subheader("GPT-4 (OpenAI)")
        st.write("A powerhouse in the AI world, renowned for its ability to generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way.")
        st.markdown("</div>", unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown("<div class='model-container'>", unsafe_allow_html=True)
        st.image("claude.png", width=200)
        st.subheader("Claude 3 Opus (Anthropic)")
        st.write("Known for its safety and helpfulness, this AI assistant is trained to be informative and comprehensive, providing summaries of factual topics or creating stories.")
        st.markdown("</div>", unsafe_allow_html=True)

# Placeholder for chat functionality 
st.write("## Chat with Your Chosen AI") 

# TODO: Add your chat implementation logic here

# Footer (optional)
st.sidebar.markdown("---")
st.sidebar.info(
    "This app showcases the capabilities of different large language models. "
    "Learn more about them: [Vertex AI](https://cloud.google.com/vertex-ai), "
    "[OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/)"
)
