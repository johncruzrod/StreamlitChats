import streamlit as st

# Page configuration (keep as before)
st.set_page_config(
    page_title="AI Chat Explorer",
    page_icon="🤖",
    layout="wide"
)

# Welcome message (keep as before)
st.title("🤖 AI Chat Explorer")
st.write("## Engage with Cutting-Edge Language Models!")

# Model descriptions with columns for better visual organization
col1, col2, col3 = st.columns(3)  # Create three columns

with col1:
    st.subheader("Gemini 1.5 Pro (Vertex AI)")
    st.write("Google's advanced language model, trained on a massive dataset, excels in understanding and responding to complex queries, generating different creative text formats, and translating languages.")

with col2:
    st.subheader("GPT-4 (OpenAI)")
    st.write("A powerhouse in the AI world, renowned for its ability to generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way.")

with col3:
    st.subheader("Claude 3 Opus (Anthropic)")
    st.write("Known for its safety and helpfulness, this AI assistant is trained to be informative and comprehensive, providing summaries of factual topics or creating stories.")

# Remove the radio buttons entirely

# Placeholder for chat functionality (you'll need to implement this)
# You can choose a default model or ask the user for input in another way
st.write("## Chat with Your Chosen AI") 

# ... Add your chat implementation logic here ...

# Footer (optional, keep as before)
st.sidebar.markdown("---")
st.sidebar.info(
    "This app showcases the capabilities of different large language models. "
    "Learn more about them: [Vertex AI](https://cloud.google.com/vertex-ai), "
    "[OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/)"
)
