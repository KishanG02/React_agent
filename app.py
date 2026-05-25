import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# ======================================
# LOAD ENV VARIABLES
# ======================================
load_dotenv()

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Fast Groq Agent",
    page_icon="⚡",
    layout="wide"
)

# ======================================
# TITLE
# ======================================
st.title("⚡ Fast Groq AI Agent")
st.caption("Ultra Fast AI Chatbot using Groq")

# ======================================
# LOAD API KEY
# ======================================
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# ======================================
# CREATE GROQ CLIENT
# ======================================
client = Groq(api_key=api_key)

# ======================================
# SESSION STATE
# ======================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================
# DISPLAY CHAT HISTORY
# ======================================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ======================================
# USER INPUT
# ======================================
prompt = st.chat_input("Ask anything...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        try:

            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": m["role"],
                        "content": m["content"]
                    }
                    for m in st.session_state.messages
                ],
                temperature=0.3,
                stream=True
            )

            for chunk in stream:

                content = chunk.choices[0].delta.content

                if content:
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

            # Save assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:
            st.error(f"Error: {e}")