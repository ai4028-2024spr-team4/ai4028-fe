import streamlit as st
from st_pages import add_page_title, hide_pages
import openai
import os 
from dotenv import load_dotenv
from PIL import Image
from streamlit_chat import message
st.set_page_config(layout="wide")
add_page_title()
hide_pages(["네트워크기반 지능 연구실"])
load_dotenv('secrets.env')
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

st.write(" We like to code. We like Big Things (Kubernetes, HPC). We like startups.")
st.write(" We like the convergence of AI with other fields.")
st.write(" We love to treat all of these like toys and do the most tech-intensive research in the world.")
st.write(" Do you think so too? Check out our playground and start your research! ")

st.header("김종원 교수님")
example_image = Image.open("example_app/jongwon.png")

st.markdown(
    """
    <style>
    .chat-history {
        height: 500px;
        overflow-y: auto;
        border: 1px solid #ddd;
        padding: 10px;
    }
    .chat-input {
        position: -webkit-sticky;
        position: sticky;
        top: -10;
        background-color: white;
        padding-bottom: 0px;
        margin-bottom: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_response(prompt):
    completions = openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    return completions.choices[0]['message']['content']

# Add the input form above the chat history
st.markdown('<div class="chat-input">', unsafe_allow_html=True)
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 3])
with col1:
    st.image(example_image, caption="김종원 교수", use_column_width=True)

with col2:
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"
        
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    if submitted and user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
        st.experimental_rerun()

    chat_history_container = st.container(height=500)
    with chat_history_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f'{i}_user')
            message(st.session_state["generated"][i], key=f'{i}_assistant')
    st.markdown('</div>', unsafe_allow_html=True)
    scroll_to_bottom = """
    <script>
    document.querySelector('.chat-history').scrollTop = document.querySelector('.chat-history').scrollHeight;
    </script>
    """
    st.markdown(scroll_to_bottom, unsafe_allow_html=True)