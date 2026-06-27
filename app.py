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

col1, col2 = st.columns(2)

with col1:
    user_age = st.number_input("Write your age:", min_value=1, max_value=100, value=25)
    existing_disease = st.selectbox("Did you have any disease in previous?", ["None", "Diabetes", "Hypertension", "Kidney Disease"])

with col2:
    symptom_days = st.slider("How many days you are suffering? (Days)", 1, 14, 3)

user_input = st.text_input("DO you want to know about specefic disease or health information")
if st.button("give the answer"):
    if user_input:
        with st.spinner("Processing with AI..."):
            context_data = load_context()

            if context_data:
                prompt2 = f"""
                You are a smart Health assistant 
                Answer the user's question based strictly on the provided Context below.
                Context:
                {context_data}

                User Question: {user_input}
                Answer:"""
                try:
                    model = genai.GenerativeModel("gemini-2.5-flash" \
                    "")
                    response2 = model.generate_content(prompt2)
                    st.success("Answer from AI:")
                    st.write(response2.text)
                except Exception as e:
                    st.error(f"Error connecting to AI: {e}")
    else:
        st.warning("Please enter a query.")

#user will write his problems in brief
user_symptoms = st.text_area("Write about your current physical or Mental problem in brief:")

if st.button("Analyze the symptoms"):
    if user_symptoms:
        with st.spinner("Processing with AI..."):
            context_data = load_context()
            
            if context_data:
                prompt = f"""You are an advanced AI Clinical Assistant under the Health & Medical Track.Your task is to analyze the user's specific health data against our Verified Medical Knowledge Base.You can use your intelligence to provide informations to the users but do not use information not related to our Verified Medical Knowledge Base.

                Verified Medical Knowledge Base:
                {context_data}

                User Profile:
                - Age: {user_age}
                - Chronic Conditions: {existing_disease}
                - Symptom Duration: {symptom_days} days
                - Current Symptoms described by user: "{user_symptoms}"

                Based STRICTLY on the knowledge base, provide a personalized advisory response including:
                1. Potential Condition (with a clear risk level: Low/Medium/High).
                2. Immediate Primary Advice / First-Aid.
                3. Referral (Which specialist doctor or hospital department they should visit).

                *Crucial Rule*: Add a clear medical disclaimer at the end."""

                

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