from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.title("サンプルアプリ③: 課題21用アプリ")

st.write("##### 動作モード1: ファッション専門家としてのチャットボット")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでファッションに関するアドバイスを受けることができます。")
st.write("##### 動作モード2: サッカーの専門家としてのチャットボット")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでサッカーに関するアドバイスを受けることができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ファッション専門家", "サッカー専門家"]
)

st.divider()

input_text = st.text_input(label="質問を入力してください。")
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
if selected_item == "ファッション専門家":
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    messages = [
        SystemMessage(content="あなたは優秀なファッション専門家です。"),
        HumanMessage(content=input_text)
    ]
    result = llm(messages)
    print(result.content)
else:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    messages = [
        SystemMessage(content="あなたは優秀なサッカー専門家です。"),
        HumanMessage(content=input_text)
    ]
    result = llm(messages)
    print(result.content)
if st.button("実行"):
    st.divider()

    if selected_item == "ファッション専門家":
        st.write("### 回答")
        st.write(result.content)
    else:
        st.write("### 回答")
        st.write(result.content)