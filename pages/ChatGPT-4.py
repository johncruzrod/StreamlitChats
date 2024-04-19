import openai
import streamlit as st

# Check if coming from a different app and reset chat
if 'last_app' not in st.session_state or st.session_state['last_app'] != 'gpt-4':
    st.session_state['gpt4_messages'] = []
    st.session_state['gpt4_thread_id'] = None

st.session_state['last_app'] = 'gpt-4'

# Initialize OpenAI client with API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to run assistant within an existing thread or create a new one
def run_assistant(question, thread_id=None):
    if thread_id is None:
        # Create a new thread if one does not exist
        thread = openai.beta.threads.create()
        thread_id = thread.id
    
    # Add user's question to the thread
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=question
    )
    # Create and poll a run
    run = openai.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id="asst_UEVqifz1E5lF4nddLXVbpbza"
    )
    # Retrieve messages only if the run is completed
    if run.status == 'completed':
        messages = openai.beta.threads.messages.list(
            thread_id=thread_id
        )
        return messages, thread_id
    else:
        return f"Run status: {run.status}", thread_id

st.set_page_config(page_title="Chat with GPT-4", layout="wide")
col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    st.title('Chat with GPT-4')
    
    # Initialize OpenAI client with API key from Streamlit secrets
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    # Streamlit UI setup
    if 'gpt4_thread_id' not in st.session_state:
        st.session_state['gpt4_thread_id'] = None
    if "gpt4_messages" not in st.session_state:
        st.session_state.gpt4_messages = []
    
    for message in st.session_state.gpt4_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    user_question = st.chat_input("What is up?")
    if user_question:
        st.session_state.gpt4_messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)
        with st.chat_message("assistant"):
            with st.spinner('Waiting for the assistant to respond...'):
                result, st.session_state['gpt4_thread_id'] = run_assistant(user_question, st.session_state['gpt4_thread_id'])
                if isinstance(result, str):
                    st.error(result)
                else:
                    for message in result:
                        if message.role == "assistant":
                            response = message.content[0].text.value
                            st.markdown(response)
                            st.session_state.gpt4_messages.append({"role": "assistant", "content": response})
                            break
