import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()
hide_pages(["LAB1"])
st.write("AI 대학원은 ~~~~ ")
st.write("This is just a sample page!?")

import streamlit as st

def generate_response(input_text):
    response = "LLM 응답: 이것은 가상의 응답입니다."
    signal = "1"  # 
    tts = "이것은 가상의 TTS입니다."
    return response, signal, tts

def main():
    example_image = "https://via.placeholder.com/300"
    col1, col2 = st.columns([2, 2])  
    with col1:
        st.image(example_image, caption="예시 이미지", use_column_width=True)
    with col2:
        st.title("채팅 앱")
        st.header("사용자 입력")

        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'enter_pressed' not in st.session_state:
            st.session_state.enter_pressed = False

        user_input = st.text_input("채팅 입력란", "")

        if st.session_state.enter_pressed:
            st.session_state.chat_history.append(user_input)
            user_input = ""  # 입력A칸 초기화

        st.write("대화 내용:")
        for chat in st.session_state.chat_history:
            st.text("사용자: " + chat)

        if user_input:
            st.session_state.enter_pressed = True
            if st.button("전송"):
                st.session_state.enter_pressed = True
                response, signal, tts = generate_response(user_input)
                st.write(response)  # LLM 응답 출력
                # TTS? 
                # GIF 1~,,,?
                if signal == "1":
                    example_image = "https://via.placeholder.com/300"
                    st.image(example_image, caption="신호 1에 대한 이미지", use_column_width=True)

if __name__ == "__main__":
    main()

# import streamlit as st

# example_image = "https://via.placeholder.com/300"
# col1, col2 = st.columns([2, 2])  # 컬럼을 생성하여 비율을 조정
# with col1:
#     st.image(example_image, caption="예시 이미지", use_column_width=True)
# # 채팅 창
# with col2:
#     st.title("채팅 앱")
#     st.header("사용자 입력")

#     # 상태를 초기화
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []
#     if 'enter_pressed' not in st.session_state:
#         st.session_state.enter_pressed = False

#     # 사용자 입력 받기
#     user_input = st.text_input("채팅 입력란", "")

#     # 사용자가 입력을 제출했을 때
#     if st.session_state.enter_pressed:
#         st.session_state.chat_history.append(user_input)
#         user_input = ""  # 입력A칸 초기화

#     # 채팅 창에 대화 표시
#     st.write("대화 내용:")
#     for chat in st.session_state.chat_history:
#         st.text("사용자: " + chat)

#     # Enter 키 이벤트 처리
#     if user_input:
#         st.session_state.enter_pressed = True
#         if st.button("전송"):
#             st.session_state.enter_pressed = True
            