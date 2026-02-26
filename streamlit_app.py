# app.py

import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="HF AI Agent Pro",
    page_icon="🤖",
    layout="wide",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.chat-bubble-user {
    background: #2563eb;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 8px;
}

.chat-bubble-bot {
    background: #111827;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 8px;
    border: 1px solid #374151;
}

.stTextInput > div > div > input {
    background-color: #020617;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("🤖 Open-Source AI Agent")
st.caption("⚡ Hugging Face • Tool-Calling • Production UI")

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Chat Display ----------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="chat-bubble-user">🧑 {msg["content"]}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="chat-bubble-bot">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True,
        )

# ---------- Input ----------
user_input = st.chat_input("Ask anything…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Agent thinking..."):
        response = run_agent(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()