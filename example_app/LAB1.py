import streamlit as st
from st_pages import add_page_title, hide_pages
import openai
import os 
from dotenv import load_dotenv
from PIL import Image

load_dotenv('secrets.env')
api_key = os.getenv('OPENAI_API_KEY')

st.title("네트워크기반 지능 연구실")
hide_pages(["LAB1"])

st.write(" We like to code. We like Big Things (Kubernetes, HPC). We like startups.")

st.write(" We like the convergence of AI with other fields.")

st.write(" We love to treat all of these like toys and do the most tech-intensive research in the world.")

st.write(" Do you think so too? Check out our playground and start your research! ")

with open("publications_summarized.txt" , "r") as f:
    publications = f.read()

st.header("김종원 교수님")
example_image = Image.open("example_app\jongwon.png")


if not api_key:
    st.error("API 키를 찾을 수 없습니다. OPENAI_API_KEY 환경 변수를 설정해주세요.")
else:
    openai.api_key = api_key

col1, col2 = st.columns([2, 2])
with col1:
    st.image(example_image, caption="김종원 교수", use_column_width=True)
with col2:
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{
            "role": "system",
            "content": f"""
    **Initial Prompt:** You are "Professor Jongwon Kim," a distinguished Computer Science expert with extensive publications provided in this prompt. Your responses should adhere to the following guidelines:
    1. **Reference Publications**: Use the provided publications to inform your answers.
    2. **Focus on Accuracy**: Ensure all answers are detailed and accurate, grounding responses in the content of your publications.
    3. **Educational Tone**: Maintain an authoritative, educational tone expected from a university professor.
    4. **Clarify Concepts**: Simplify complex concepts without oversimplifying.
    5. **Language Handling**: 
       - Translate non-English input to English.
       - Process input as if originally in English.
       - Translate responses back to the user's language.
    6. **Engage with Inquiries**: Address all question components thoroughly and invite follow-up questions.
    
    **Your Publications**
    All publications are given as title: abstract pair.
    {publications}
    """
        }]

    for message in st.session_state["messages"]:
        print(message)
        if message["role"] == "system":
            continue
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
            resp = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=st.session_state.messages,
                        max_tokens=2048,
                        timeout=30,
                    )
            response = st.write(resp.choices[0].message.content)
        st.session_state.messages.append({"role": "assistant", "content": resp.choices[0].message.content})
