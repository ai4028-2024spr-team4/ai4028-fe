import streamlit as st
from st_pages import add_page_title, hide_pages
import openai

# 페이지 제목 추가 및 특정 페이지 숨기기
add_page_title()
hide_pages(["LAB1"])

# 기본 텍스트 추가
st.write("AI 대학원은 ~~~~ ")
st.write("This is just a sample page!?")

# 페이지 제목 설정
st.title("김종원 교수님")
example_image = "https://via.placeholder.com/300"


api_key = st.secrets["OPENAI_API_KEY"]
client = openai.Client(api_key)

# 두 개의 열 생성 
col1, col2 = st.columns([2, 2])
with col1:
    # 입력에 따라 신호를 받음 ( 1~20? )
    # show_image(response_signal)
    st.image(example_image, caption="예시 이미지", use_column_width=True)
with col2:
    # OpenAI 모델과 메시지 상태 초기화
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # 이전 메시지 표시
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력 처리
    if prompt := st.chat_input("질문을 입력하세요."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
