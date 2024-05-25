import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()
st.write("AI 대학원은 ~~~~ ")

import streamlit as st

def app():
    st.title("AI 대학원")
    if st.button("Go to 물리광과학과"):
        st.experimental_set_query_params(page="물리광과학과")
    if st.button("Go to 의생명공학부"):
        st.experimental_set_query_params(page="의생명공학부")
    if st.button("Go to 전기전자컴퓨터공학부"):
        st.experimental_set_query_params(page="전기전자컴퓨터공학부")

