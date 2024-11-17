import streamlit as st
import google.generativeai as genai
import os
#genai.configure(api_key="AIzaSyBg3WQZ_CB0SwnKhC7xtbljK-E6_ILG1rs")

api_key = os.getenv("GENAI_API_KEY")
if api_key is None:
    st.error("API key is not set. Please configure the GENAI_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

sys_prompt="""You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaininf a concept.
Incase if a student asks any question outside the datascience scope, 
polietely decline and tell the to ask question from the data science domain only."""

model=genai.GenerativeModel(model_name="models/gemini-1.5-flash",system_instruction=sys_prompt)



st.title("Data Science Tuitor Application")
user_prompt=st.text_input("Enter your query:", placeholder="Type your query here...")
btn_click=st.button("Generate Answer")
if btn_click==True:
    response=model.generate_content(user_prompt)
    st.write(response.text)