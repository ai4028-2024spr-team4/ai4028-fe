import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()
hide_pages(["LAB1"])
st.write("AI 대학원은 ~~~~ ")

import streamlit as st

# 페이지 제목
st.markdown("<h1 style='font-size: 24px; font-weight: bold; color: #4B8BBE;'>연구실 목록</h1>", unsafe_allow_html=True)

# CSS 스타일을 지정합니다.
st.markdown(
    """
    <style>
        /* 제목 스타일 수정 */
        .title {
            font-size: 24px !important;
            margin-bottom: 20px !important;
        }
        /* 섹션 스타일 수정 */
        .section {
            margin-bottom: 30px !important;
        }
        /* 버튼 스타일 수정 */
        .button {
            font-size: 14px !important;
            padding: 10px 15px !important;
            margin-bottom: 10px !important;
            border-radius: 5px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

majors = {
    "연구실1": {
        "description": "AI대학원에 대한 설명입니다. AI 대학원은 ~~~~ , ~~~ , ~~~,  ~~~~, ~~",
        "homepage": "https://ai.university.example",
        "next_page": "example_app/LAB1.py"
    },
    "연구실2": {
        "description": "물리광과학과에 대한 설명입니다.",
        "homepage": "https://physics.university.example",
        "next_page": "example_app//.py"
    },
    "연구실3": {
        "description": "전기전자컴퓨터공학부에 대한 설명입니다.",
        "homepage": "https://eece.university.example",
        "next_page": "example_app//.py"
    },
    "연구실4": {
        "description": "의생명공학부에 대한 설명입니다.",
        "homepage": "https://biomedical.university.example",
        "next_page": "example_app//.py"
    }
}

for major, info in majors.items():
    st.markdown(f"<div class='section'><h2>{major}</h2><p>{info['description']}</p></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])  # 왼쪽 칸은 3/4의 너비, 오른쪽 칸은 1/4의 너비
    with col1:
        st.write(f"[{major} 홈페이지]({info['homepage']})", key=f"{major}_homepage", 
                 help=f"{major} 홈페이지로 이동합니다.", 
                 **{"class": "stButton", "style": "display: none;"})        
    with col2:
        if st.button(f"자세히 알아보기", key=f"{major}_next"):
            st.switch_page(info['next_page'])

