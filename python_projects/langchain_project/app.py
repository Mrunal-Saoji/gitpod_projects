import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title('GPT CREATOR')
prompt = st.text_input('Plug your prompt here')

