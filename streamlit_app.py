from pathlib import Path

import streamlit as st

st.title("나만의 작은 교수님")
from st_pages import Page, add_page_title, show_pages, Section, hide_pages

show_pages(
        [   Page("streamlit_app.py", "Home", icon=":🏠:"),
            # Can use :<icon-name>: or the actual icon
            Section(name="전공목록"),
            # The pages appear in the order you pass them
            Page("example_app/AI대학원.py", "AI대학원"),
            Page("example_app/물리광과학과.py", name="물리광과학과"),
            # Will use the default icon and name based on the filename if you don't
            # pass them
            Page("example_app/전기전자컴퓨터공학부.py", "전기전자컴퓨터공학부"),
            Page("example_app/의생명공학부.py", "의생명공학부"),
            Page("example_app/LAB1.py", "LAB1"), 
        ]
)
hide_pages(["LAB1"])

add_page_title()  # Optional method to add title and icon to current page


"#광주과학기술원은 ~~~~ ."
"#그래서 우리는 ~~~하는 웹사이트를 통해 ~~하려고 한다."


# 페이지 제목
st.markdown("<h1 style='font-size: 24px; font-weight: bold; color: #4B8BBE;'>전공 목록</h1>", unsafe_allow_html=True)

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
    "AI대학원": {
        "description": "AI대학원에 대한 설명입니다. AI 대학원은 ~~~~ , ~~~ , ~~~,  ~~~~, ~~",
        "homepage": "https://ai.university.example",
        "next_page": "example_app/AI대학원.py"
    },
    "물리광과학과": {
        "description": "물리광과학과에 대한 설명입니다.",
        "homepage": "https://physics.university.example",
        "next_page": "example_app/물리광과학과.py"
    },
    "전기전자컴퓨터공학부": {
        "description": "전기전자컴퓨터공학부에 대한 설명입니다.",
        "homepage": "https://eece.university.example",
        "next_page": "example_app/전기전자컴퓨터공학부.py"
    },
    "의생명공학부": {
        "description": "의생명공학부에 대한 설명입니다.",
        "homepage": "https://biomedical.university.example",
        "next_page": "example_app/의생명공학부.py"
    }
}
# 1안
# for major, info in majors.items():
#     st.markdown(f"<div class='section'><h2>{major}</h2><p>{info['description']}</p></div>", unsafe_allow_html=True)
#     st.write(f"[{major} 홈페이지]({info['homepage']})", key=f"{major}_homepage", 
#              help=f"{major} 홈페이지로 이동합니다.", 
#              **{"class": "stButton", "style": "display: none;"})
#     button_clicked = st.button(f"{major} 연구실 목록", key=f"{major}_next")
#     if button_clicked:
#         st.switch_page(info['next_page'])

for major, info in majors.items():
    st.markdown(f"<div class='section'><h2>{major}</h2><p>{info['description']}</p></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])  # 왼쪽 칸은 3/4의 너비, 오른쪽 칸은 1/4의 너비
    with col1:
        st.write(f"[{major} 홈페이지]({info['homepage']})", key=f"{major}_homepage", 
                 help=f"{major} 홈페이지로 이동합니다.", 
                 **{"class": "stButton", "style": "display: none;"})        
    with col2:
        if st.button(f"{major} 연구실 목록", key=f"{major}_next"):
            st.switch_page(info['next_page'])
