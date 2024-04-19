import streamlit as st

# Improved page configuration
st.set_page_config(
    page_title="AI Chat Explorer",  # More descriptive title
    page_icon="🤖",  # Robot emoji for icon
    layout="wide",  # Use wide layout for better visual appeal
)

# Enhanced welcome message with title and emoji
st.title("🤖 AI Chat Explorer")
st.write("## Engage with Cutting-Edge Language Models!")

# Model descriptions in an expandable container for better organization
with st.expander("Explore the Models:"):
    st.markdown(
        """
        **Choose your AI companion and experience the future of conversation!**

        **Gemini 1.5 Pro (Vertex AI):** Google's advanced language model, trained on a massive dataset, excels in understanding and responding to complex queries, generating different creative text formats, and translating languages.

        **GPT-4 (OpenAI):** A powerhouse in the AI world, renowned for its ability to generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way.

        **Claude 3 Opus (Anthropic):**  Known for its safety and helpfulness, this AI assistant is trained to be informative and comprehensive, providing summaries of factual topics or creating stories. 
        """
    )

# Sidebar with model selection
st.sidebar.title("Select Your AI:")
model_selection = st.sidebar.radio(
    "", options=["Gemini 1.5 Pro", "GPT-4", "Claude 3 Opus"]
)

# Placeholder for chat functionality based on selected model
st.write(f"## You've chosen: {model_selection}")
# Add your chat implementation logic here based on the selected model

# Footer with information and links (optional)
st.sidebar.markdown("---")
st.sidebar.info(
    "This app showcases the capabilities of different large language models. "
    "Learn more about them: [Vertex AI](https://cloud.google.com/vertex-ai), "
    "[OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/)"
)
