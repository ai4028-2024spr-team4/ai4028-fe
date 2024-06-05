import streamlit as st
from st_pages import add_page_title, hide_pages
import openai
import os 
from dotenv import load_dotenv
from PIL import Image
import base64
import streamlit.components.v1 as components
from kiwipiepy import Kiwi
from langdetect import detect
kiwi = Kiwi()
import requests
from urllib import parse
from pydub import AudioSegment
# from sound import text_to_speech

current_wav = 0

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true" style="display:none">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

load_dotenv('secrets.env')
api_key = os.getenv('OPENAI_API_KEY')
add_page_title()


st.write(" We like to code. We like Big Things (Kubernetes, HPC). We like startups.")

st.write(" We like the convergence of AI with other fields.")

st.write(" We love to treat all of these like toys and do the most tech-intensive research in the world.")

st.write(" Do you think so too? Check out our playground and start your research! ")


with open("publications_summarized.txt" , "r", encoding='utf-8') as f:
    publications = f.read()

st.header("김종원 교수님")
example_image = Image.open("example_app/jongwon.png")

if not api_key:
    st.error("API 키를 찾을 수 없습니다. OPENAI_API_KEY 환경 변수를 설정해주세요.")
else:
    openai.api_key = api_key

col1, col2 = st.columns([1, 2])
with col1:
    st.image(example_image, caption="김종원 교수", use_column_width=True)

if prompt := st.chat_input("질문을 입력하세요."):
            st.session_state["messages"].append({"role": "user", "content": prompt})    
            with st.spinner("메시지 처리 중입니다."):
                resp = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=st.session_state.messages,
                            max_tokens=2048,
                            timeout=30,
                        )
                response = resp.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": resp.choices[0].message.content})
            # speech_file_path = text_to_speech(resp.choices[0].message.content)
            #speech_file_path = "example_app/train.wav"
            #autoplay_audio(speech_file_path)
            # os.remove(speech_file_path)

with col2:
        chat_history_container = st.container(height=500)

        with chat_history_container :
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
                if message['role'] =="assistant" and (detect(message['content']) == "ko"):
                    # 코드 변환 - 한국어를 그대로 보낼 수 없으므로 아래 방식으로 변환 필요.
                    
                    word_list = kiwi.split_into_sents(message['content'])
                    current_wav = len(word_list)
                    for i in range(len(word_list)):
                        texts = word_list[i].text.replace("*","")
                        print(texts)
                        encode  = parse.quote(texts)
                        headers = {}
                        json_data = {'text': encode,}

                        response = requests.post('http://127.0.0.1:5000/predict', headers=headers, json=json_data)

                        with open(f'output{i}.wav', 'wb') as f:
                            f.write(response.content)
                        

                    wav_files = ['audio1.wav', 'audio2.wav', 'audio3.wav']
                    combined_audio = AudioSegment.from_wav(f'output0.wav')
                    for i in range(1, current_wav):
                        next_audio = AudioSegment.from_wav(f'output{i}.wav')
                        combined_audio += next_audio                       
                    combined_audio.export("output.wav", format="wav")
                        
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
                    if message['role'] =="assistant" and (detect(message['content']) == "ko"):
                        autoplay_audio("./output.wav")
