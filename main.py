import os
import openai
# from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
import time

# load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')
chat_model = ChatOpenAI(openai_api_key=api_key)

st.title('시를 써보자')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')


title = st.text_input('어떤 내용의 시를 써줄까?')
st.write( title, '에 대한 시를 써줄게')


if st.button('시 작성'):
    with st.spinner('Wait for it...'):
        result = chat_model.predict(title + "에 대한 시를 써줘")
        st.write(result)


# print(result)

#llm = ChatOpenAI()