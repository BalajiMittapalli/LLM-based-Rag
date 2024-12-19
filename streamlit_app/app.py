import streamlit as st
import requests
import time
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


st.set_page_config(
    page_title="LLM-based RAG Search",
    page_icon="\U0001F4AC",  
    layout="centered",
)

st.title("\U0001F4AC LLM-based RAG Search")
st.subheader("Interact with a Retrieval-Augmented Generation (RAG) system")

if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_chat' not in st.session_state:
    st.session_state.current_chat = []
if 'query' not in st.session_state:
    st.session_state.query = ""

def summarize_chat(chat):
    if chat:
        first_query = chat[0].get('query', 'New Chat')
        return first_query if len(first_query) <= 30 else first_query[:30] + '...'
    return "New Chat"

with st.sidebar:
    st.header("Chat History")

    for i, chat in enumerate(st.session_state.history):
        chat_title = summarize_chat(chat)
        if st.button(chat_title, key=f"load_chat_{i}"):
            st.session_state.current_chat = chat
            st.session_state.memory = ConversationBufferMemory(return_messages=True)
            for entry in chat:
                st.session_state.memory.chat_memory.add_user_message(entry['query'])
                st.session_state.memory.chat_memory.add_ai_message(entry['response'])
            st.session_state.query = ""

    if st.button("+ New Chat"):
        st.session_state.current_chat = []
        st.session_state.memory = ConversationBufferMemory(return_messages=True)
        st.session_state.query = ""

query = st.text_input(
    "Type your question below:",
    key="query_input",
    value=st.session_state.query,  # Bind session state to the input field
    placeholder="Ask your question...",
    on_change=lambda: st.session_state.update({"query": st.session_state.query_input}),
)

submit = st.button("Submit")
# Display previous chat messages
st.markdown("### Chat Conversation")
if st.session_state.current_chat:
    for msg in st.session_state.current_chat:
        if msg['query']:
            st.markdown(f"**You:** {msg['query']}")
        if msg['response']:
            st.markdown(f"**Bot:** {msg['response']}")

def display_animated_response(answer):
    response_container = st.empty()
    current_text = ""
    for word in answer.split():
        current_text += word + " "
        response_container.markdown(f"**Answer:** {current_text}")
        time.sleep(0.05)  
    return current_text

if submit:  
    if query:
        with st.spinner("Fetching response..."):
            response = requests.post('http://localhost:5001/query', json={'query': query})
            if response.status_code == 200:
                answer = response.json().get('response', 'No answer received.')
                final_response = display_animated_response(answer)
                st.session_state.memory.chat_memory.add_user_message(query)
                st.session_state.memory.chat_memory.add_ai_message(final_response)
                st.session_state.current_chat.append({"query": query, "response": final_response})
                if st.session_state.current_chat not in st.session_state.history:
                    st.session_state.history.append(st.session_state.current_chat)
                st.session_state.query = ""
            else:
                st.error(f"Error: Unable to get a response from the API. Status Code: {response.status_code}")
    else:
        st.warning("Please enter a question before submitting.")

st.markdown(
    """
    <style>
        .stTextInput {
            margin-bottom: 20px;
        }
        .stMarkdown {
            font-family: 'Courier New', monospace;
            background: #000000;
            color: #FFFFFF;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)
