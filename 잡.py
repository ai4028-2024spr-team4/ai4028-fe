import streamlit as st

# 웹사이트 제목과 설명
st.title("내 웹사이트")
st.write("이 웹사이트는 Streamlit을 사용하여 만들어졌습니다.")

from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("other_pages/page2.py", "Page 2", ":books:"),
    ]
)
style = """
<style>
.custom-block {
    background-color: #f0f0f5;
    border-left: 4px solid #4CAF50;
    padding: 10px;
    margin: 10px 0;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.custom-block .small-block {
    background-color: #f9f9f9;
    padding: 10px;
    flex-grow: 1;
    box-shadow: none;
    display: flex;
    align-items: center;
    justify-content: center;
}

.custom-flex {
    display: flex;
    align-items: stretch;
    height: 200px; /* 높이를 원하는 만큼 설정 */
}

.custom-flex img {
    max-width: 200px;
    margin-right: 20px;
    height: 100%; /* 이미지가 컨테이너의 높이를 채우도록 설정 */
    object-fit: cover; /* 이미지가 왜곡되지 않도록 비율 유지 */
}

.custom-flex .small-block {
    background-color: #f9f9f9;
    padding: 10px;
    flex-grow: 1;
    box-shadow: none;
    display: flex;
    align-items: center;
    justify-content: center;
}

.bold-text {
font-weight: bold;
}

</style>
"""

# HTML 내용 정의
html_content = """
<div class="custom-block">
    <p>나만의 작은 교수님 웹사이트 사용방법:</p>
    <p>   1. 전공 및 연구실 선택 </p>
    <div class="custom-flex">
        <img src="https://via.placeholder.com/100" alt="Sample Image">
        <div class="small-block">
            <p> 좌측 전공 목록에서 관심있는 분야의 전공을 선택하여 전공 페이지로 들어간다. <br> 분야별 연구실 목록에서 알고싶은 연구실을 선택한다.</p>
        </div>        
    </div>
    <p>   <br> 2. 연구실 정보보기 / 교수님과 대화하기 </p>
    <div class="custom-flex">
        <img src="https://via.placeholder.com/100" alt="Sample Image">
        <img src="https://via.placeholder.com/100" alt="Sample Image">
        </div>
    <br>
    <div class="small-block">
        <p> 위 사진의 정보보기 버튼을 통해 ~ <br> 혹은 대화하기 버튼을 통해 ~ </p>
    </div>
</div>
"""

# 스타일과 HTML을 적용
st.markdown(style, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
