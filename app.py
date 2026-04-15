import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") # instead of getenv, you can use os.environ.get as well

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Write a python program to print 'Hello, World!'"
)

st.write(response.text)
