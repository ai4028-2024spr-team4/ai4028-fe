import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()
hide_pages(["LAB1"])
st.write("광주과학기술원 AI대학원은 인공지능의 핵심기술을 이해하고 다양한 분야의 인재와 협력하여, 기업이 직면한 문제의 창의적 해결 및 AI를 활용한 사업화/창업 등을 통해 새로 운 공동가치를 창출할 수 있는 AI융합 인재 양성을 목표로 한다. 이를 위해 본 대학원은 T.R.A.I.N. 교육과 G.I.S.T. AI for X 연구를 통해 AI인재를 육성한다. T.R.A.I.N.은 학생 들에게 자기주도적으로(Teaching yourself) 즐겁게(Recreation) 학습하고 신기술에 빠르게 적응하며(Adaptation) 탁월한 현장감각을(Industrial) 바탕으로 새로운 가치창 출(New value)을 할 수 있는 소양을 겸비하도록 하는 교육이고, G.I.S.T. AI for X는 학 생들이 스스로 학습하여(Generalizable) 통합하고(Integrated) 안전/ 빠르게(Safe/ Swift.) 실행에 옮기는(Transferable) AI의 핵심 기술을 연구하고 이를 바탕으로 헬스케 어, 자동차, 에너지 분야의 융합 연구를 유기적으로 수행하여 사회적 공동 가치를 실현 할 수 있도록")

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
    "네트워크기반 지능 연구실": {
        "description": "라우드 데이터센터와 통신망 인프라가 혁신적으로 통합되면서 AI 융합 서비스의 실현이 핵심적인 기술 가치로 자리잡기 시작했다. 본 연구실은 가상화된 컴퓨팅/네트워킹/스토리지 자원들을 소프트웨어-정의 네트워크 기반 으로 연결하는 소프트웨어-정의 미래인프라의 특성을 이해하고 실증하며, 이를 바탕으로 다양한 AI 융합 서비스 들을 신속하고 경제적으로 실현하기 위하여 클라우드-네이티브 컴퓨팅 개념에 기반한 Smart (지능형) + X (유 연하게 변화하여 적응함)’을 연계하는 개방적이며 소프트웨어 중심적인 실증형 Networked Intelligence 기술 을 연구한다.",
        "homepage": "https://netai.smartx.kr/",
        "next_page": "example_app/LAB1.py"
    },
    "지능 표현 및 추론 연구실": {
        "description": "본 연구실에서는 진행하는 연구들은 “어떻게 지능을 만들까?” 에 대한 답을 구하는 것을 목표로 한다. 지능의 정의부터 시작하여 다양한 문제 환경에서의 지능의 행동을 분석하고 지능의 표현과 학습 및 추론을 위한 이론과 방 법을 개발한다. 지능의 특성 분석을 위한 문제군별 대표 문제 적용과 더불어 복잡한 실용 문제 해결 능력 검증을 위한 응용 연구를 병행한다.",
        "homepage": "https://irrlab.github.io/",
        "next_page": "example_app//.py"
    },
    "의료 인공지능 연구실": {
        "description": "의료 인공지능 연구실은 영상 및 신호 데이터를 통해 생물의 표현형과 유전적 매커니즘을 분석하고 질병의 진단, 치료 및 예방을 가능하게 하는 새로운 알고리즘 개발을 목표로 한다. 특히 본 연구실에서는 현재 인간의 뇌(예: 알츠하이머병, 파키슨병)와 다른 장기(예: 심혈관질환, 암) 연구에 초점을 두고 있다. 이를 위해 영상 처리, 유전 자 처리, EMR 처리를 진행한다.",
        "homepage": "https://aimed-lab.com/",
        "next_page": "example_app//.py"
    },
    "데이터 사이언스 연구실": {
        "description": "연구실은 인공지능 분야의 원천 기술 및 응용 연구를 진행한다. 데이터 불균형, 오픈 클래스 등의 장애물 속에 서의 효과적인 학습 방법과 함께, 논리적인 추론이 가능한 결과물을 제공할 수 있는 원천 기술을 개발하고자 한 다. 더불어 산업계와의 협업을 통해 실전 감각 및 문제 해결 능력을 갖춘 연구자의 양성을 목표로 한다.",
        "homepage": "https://sundong.kim/",
        "next_page": "example_app//.py"
    }
}

for major, info in majors.items():
    with st.expander(f"{major} 정보", expanded=True):
        st.markdown(f"<h2>{major}</h2>", unsafe_allow_html=True)
        st.write(f"<p>{info['description']}</p>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write(f"[{major} 홈페이지]({info['homepage']})", key=f"{major}_homepage", 
                    help=f"{major} 홈페이지로 이동합니다.", 
                    **{"class": "stButton", "style": "display: none;"})        
        with col2:
            if st.button(f"{major} 정보", key=f"{major}_next"):
                st.switch_page(info['next_page'])


