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

# Streamlit UI setup
st.title('Chat with GPT-4')

if 'gpt4_thread_id' not in st.session_state:
    st.session_state['gpt4_thread_id'] = None
if "user_messages" not in st.session_state:
    st.session_state.user_messages = []

# Display chat history with generated assistant responses
for user_message in st.session_state.user_messages:
    with st.chat_message("user"):
        st.markdown(user_message)
    
    with st.chat_message("assistant"):
        result, _ = run_assistant(user_message, st.session_state['gpt4_thread_id'])
        if isinstance(result, str):
            st.error(result)
        else:
            for message in result:
                if message.role == "assistant":
                    response = message.content[0].text.value
                    st.markdown(response)
                    break

user_question = st.chat_input("What is up?")
if user_question:
    st.session_state.user_messages.append(user_question)
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
                        break
