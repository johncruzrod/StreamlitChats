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

# Model descriptions with columns, containers, and images
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():  # Container for Gemini
        st.subheader("Gemini 1.5 Pro (Vertex AI)")
        st.write("Google's advanced language model, trained on a massive dataset, excels in understanding and responding to complex queries, generating different creative text formats, and translating languages.")
        st.image("gemini.png", width=200)  # Assuming images are in the root folder

with col2:
    with st.container():  # Container for GPT-4
        st.subheader("GPT-4 (OpenAI)")
        st.write("A powerhouse in the AI world, renowned for its ability to generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way.")
        st.image("gpt4.png", width=200)

with col3:
    with st.container():  # Container for Claude
        st.subheader("Claude 3 Opus (Anthropic)")
        st.write("Known for its safety and helpfulness, this AI assistant is trained to be informative and comprehensive, providing summaries of factual topics or creating stories.") 
        st.image("claude.png", width=200)

# Placeholder for chat functionality (you'll need to implement this)
# You can choose a default model or ask the user for input in another way
st.write("## Chat with Your Chosen AI") 

# ... Add your chat implementation logic here ...

# Footer (optional)
st.sidebar.markdown("---")
st.sidebar.info(
    "This app showcases the capabilities of different large language models. "
    "Learn more about them: [Vertex AI](https://cloud.google.com/vertex-ai), "
    "[OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/)"
)
