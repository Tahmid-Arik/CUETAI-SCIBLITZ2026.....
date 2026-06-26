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


st.title("My Streamlit App-SciBlitz 2026")
st.subheader("I am Tahmid Arik. Welcome to my AI application!")


DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "cuet_info.txt")

def load_context():
    if os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return file.read()
    else:
        st.error("Data file missing! Please create 'data/cuet_info.txt'")
        return ""

user_input = st.text_input("Ask me anything about CUET!")

if st.button("give the answer"):
    if user_input:
        with st.spinner("Processing with AI..."):
            context_data = load_context()
            
            if context_data:
                prompt = f"""
                You are a smart university assistant for CUET. 
                Answer the user's question based strictly on the provided Context below.
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