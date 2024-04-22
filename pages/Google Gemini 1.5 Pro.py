import streamlit as st
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

# Load the service account credentials from Streamlit secrets
service_account_info = {
    "type": st.secrets["gcp"]["type"],
    "project_id": st.secrets["gcp"]["project_id"],
    "private_key_id": st.secrets["gcp"]["private_key_id"],
    "private_key": st.secrets["gcp"]["private_key"],
    "client_email": st.secrets["gcp"]["client_email"],
    "client_id": st.secrets["gcp"]["client_id"],
    "auth_uri": st.secrets["gcp"]["auth_uri"],
    "token_uri": st.secrets["gcp"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gcp"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gcp"]["client_x509_cert_url"]
}

# Create credentials object
credentials = service_account.Credentials.from_service_account_info(service_account_info)

# Initialize Vertex AI SDK
vertexai.init(project=service_account_info["project_id"], location="us-central1", credentials=credentials)

# Load the model
model = GenerativeModel("gemini-1.5-pro-preview-0409")

# Set up generation configuration
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

# Set up safety settings
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Streamlit UI setup
st.title('Chat with Gemini')

if 'gemini_chat' not in st.session_state:
    st.session_state.gemini_chat = model.start_chat()

if "gemini_messages" not in st.session_state:
    st.session_state.gemini_messages = []

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []  # Initialize conversation history

# File upload
uploaded_files = st.file_uploader("Choose files", type=["jpg", "jpeg", "png", "mp4", "pdf", "mp3", "wav"], accept_multiple_files=True)
file_parts = []  # Initialize file_parts outside the if block

if uploaded_files:
    file_contents = [file.read() for file in uploaded_files]
    file_names = [file.name for file in uploaded_files]
    for file_content, file_name in zip(file_contents, file_names):
        mime_type = None
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            mime_type = "image/jpeg"
        elif file_name.lower().endswith('.mp4'):
            mime_type = "video/mp4"
        elif file_name.lower().endswith('.pdf'):
            mime_type = "application/pdf"
        elif file_name.lower().endswith(('.mp3', '.wav')):
            mime_type = "audio/mpeg"
        if mime_type is None:
            raise ValueError("Unsupported file type")
        file_parts.append(Part.from_data(mime_type=mime_type, data=file_content))
    st.session_state.conversation_history.append(f"user: Uploaded files: {', '.join(file_names)}")  # Update history with uploaded files

for message in st.session_state.gemini_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("What is up?")
if user_input:
    st.session_state.gemini_messages.append({"role": "user", "content": user_input})
    st.session_state.conversation_history.append(f"user: {user_input}")  # Update history

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner('Waiting for the assistant to respond...'):
            response = st.session_state.gemini_chat.send_message(
                st.session_state.conversation_history + file_parts,  # Include files and conversation history
                generation_config=generation_config,
                safety_settings=safety_settings
            )
            if isinstance(response, str):
                st.error(response)
            else:
                response_text = response.candidates[0].content.parts[0].text
                st.markdown(response_text)
                st.session_state.gemini_messages.append({"role": "assistant", "content": response_text})
                st.session_state.conversation_history.append(f"assistant: {response_text}")  # Update history
