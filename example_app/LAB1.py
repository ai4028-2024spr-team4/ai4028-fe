import streamlit as st
from st_pages import add_page_title, hide_pages
import openai
import os 
from dotenv import load_dotenv

load_dotenv('secrets.env')

add_page_title()
hide_pages(["LAB1"])

st.write("AI 대학원은 ~~~~ ")
st.write("This is just a sample page!?")

st.title("김종원 교수님")
example_image = "https://via.placeholder.com/300"

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    st.error("API 키를 찾을 수 없습니다. OPENAI_API_KEY 환경 변수를 설정해주세요.")
else:
    openai.api_key = api_key

col1, col2 = st.columns([2, 2])
with col1:
    st.image(example_image, caption="예시 이미지", use_column_width=True)
with col2:
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("질문을 입력하세요."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):        
            message_placeholder = st.empty() # DeltaGenerator 반환
            full_response = ""
        with st.spinner("메시지 처리 중입니다."):
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                prompt=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(response)
        st.session_state.messages.append({"role": "assistant", "content": response})