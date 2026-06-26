import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(DOTENV_PATH)


api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API Key not found! Please set GEMINI_API_KEY in your .env file.")


st.title("Health and Medical Care App-SciBlitz 2026")
st.subheader("Welcome to my AI application!Do you have Any questions about your Health or you want to know about a disease? Ask me anything and I will try to provide you with the best possible answer based on the information available in my context file.")


DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "disease_info.txt")

def load_context():
    if os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return file.read()
    else:
        st.error("Data file missing! Please create 'data/disease_info.txt'")
        return ""

user_input = st.text_input("write your info here")

if st.button("give the answer"):
    if user_input:
        with st.spinner("Processing with AI..."):
            context_data = load_context()
            
            if context_data:
                prompt = f"""
                You are a smart Health and Medical assistant for Humans.If a user gives the symptoms of a disease, you will provide the most likely disease name and its treatment according to the context below. If the user asks about a specific disease, you will provide detailed information about that disease, including its symptoms, causes, and treatment options according to the context below. If the user asks for general health advice, you will provide tips for maintaining good health and preventing illness according to the context below.You can use your own intelligence to provide the user information within the context below but do not go outside the contewxt.
                Context:
                {context_data}

                User Question: {user_input}
                Answer:
                """
                try:
                    model = genai.GenerativeModel("gemini-2.5-flash" \
                    "")
                    response = model.generate_content(prompt)
                    st.success("Answer from AI:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error connecting to AI: {e}")
    else:
        st.warning("Please enter a query.")