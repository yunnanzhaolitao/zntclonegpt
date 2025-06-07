import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_chat_response

st.title("znt的克隆chatGPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key",type="password")
    st.markdown("[获取密钥](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai","content":"你好主人，我是你的AI助手"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt=st.chat_input()
if prompt :
    if not openai_api_key:
        st.info("请输入您的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中..."):
        response = get_chat_response(prompt,st.session_state["memory"],openai_api_key)
    msg={"role":"ai","content":response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)