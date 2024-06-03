from pathlib import Path

import streamlit as st
# asd

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


"광주과학기술원(GIST)는 세계적인 경쟁력을 갖춘 글로벌캠퍼스로, 과학기술 인재양성에 초점을 맞추고 있습니다. 혁신적인 연구와 창의적인 교육을 통해 학생들을 세계 수준의 인재로 성장시키며, 다양한 분야에서 우수한 연구 성과를 거두고 있습니다. 또한 창업 지원을 통해 연구 성과를 실용적인 결과물로 이끌어내며, 국내외에서 미래를 이끌어가는 중요한 역할을 하고 있습니다."
"#본 웹사이트는 GIST 대학원의 분야와 분야별 연구실에 대한 정보를 글/채팅봇을 통해 제공하여 컨텍하는 학생들에게 편의를 제공하고자 한다."


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
        "description": "이 대학원은 T.R.A.I.N. 교육과 G.I.S.T. AI for X 연구를 통해 AI 인재를 육성하며, 자기주도적 학습과 현장감각을 갖추고, 다양한 AI 기술을 활용하여 문제를 해결하는 능력을 갖춘 AI 융합 인재를 양성합니다. AI 융합 인재는 새로운 문제를 발견하고 해결하는 문제 해결력, 고급 AI 기술과 창의적 사고를 갖추는 기술력, 그리고 다양한 사람들과 의사소통하며 사업화와 창업을 추진할 수 있는 사업화 능력을 갖추게 됩니다.",
        "homepage": "https://ai.university.example",
        "next_page": "example_app/AI대학원.py"
    },
    "물리광과학과": {
        "description": "이 학과는 첨단 연구시설을 활용해 물리학 및 광과학 분야의 세계적 연구 인력을 양성하고, 나노과학과 펨토과학을 연구합니다. 물리 및 광과학 지식을 다양한 분야에 적용해 창의적인 융합기술을 개발하며, 미래 기술을 개척할 전문 인력을 배출합니다. 고등광기술연구소와 IBS 초강력 레이저과학 연구단이 참여하여 인력양성 사업을 수행합니다.",
        "homepage": "https://physics.university.example",
        "next_page": "example_app/물리광과학과.py"
    },
    "전기전자컴퓨터공학부": {
        "description": "본 학부는 인공지능, 빅데이터, 클라우드컴퓨팅, 바이오 정보 등 첨단 기술 분야에서 연구를 선도하며, 전기전자컴퓨터 분야의 중요한 산업을 주도할 핵심 기술 개발에 집중합니다. 다양한 학문 분야의 석·박사 학생들이 협력하여 창의적 연구를 수행하고, 이를 통해 국가의 미래를 이끌 과학기술 인재를 양성합니다. BK21플러스사업, 노벨연구센터 등 여러 연구센터와의 협력을 통해 세계적 연구와 기술 상용화에 앞장서고 있습니다.",
        "homepage": "https://eece.university.example",
        "next_page": "example_app/전기전자컴퓨터공학부.py"
    },
    "의생명공학부": {
        "description": "이 학과는 첨단 연구시설을 활용해 물리학 및 광과학 분야의 세계적 연구 인력을 양성하고, 나노과학과 펨토과학을 연구합니다. 물리 및 광과학 지식을 다양한 분야에 적용해 창의적인 융합기술을 개발하며, 미래 기술을 개척할 전문 인력을 배출합니다. 고등광기술연구소와 IBS 초강력 레이저과학 연구단이 참여하여 인력양성 사업을 수행합니다.",
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
