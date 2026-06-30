import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables explicitly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(DOTENV_PATH)

# Fetch single active API key
api_key = os.getenv("GEMINI_API_KEY")

st.title("Health and Medical Care App-SciBlitz 2026")
st.subheader("Welcome to our Health& Medical service AI application.Do you have Any questions about your Health or you want to know about a disease? Ask me anything and I will try to provide you with the best possible answer based on the information available in my context file.")

DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "disease_info.txt")

@st.cache_data
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

# User symptoms input
user_symptoms = st.text_area("Write about your current physical or Mental problem in brief:")

if st.button("Answer"):
    if user_symptoms:
        if not api_key:
            st.error("API Key not found! Please set GEMINI_API_KEY in your .env file.")
        else:
            with st.spinner("Processing with AI...(wait for a while)"):
                context_data = load_context()
                
                if context_data:
                    prompt = f"""You are a Clinical AI Assistant under the Health & Medical Track for Bangladesh.Answer the question of the user by using your own intelligence but within our {context_data} is mandatory for you.
                Context Database:
                {context_data}
                if user ask you any health or medical information for gaining knowledge,describe him/her in brief with coherent paragraphs
                User profile:[use this profile only if the user ask you to evaluate his/her diseases]
                1.Age: {user_age}years
                2.Pre-existing: {existing_disease}
                3.Duration: {symptom_days} days
                4.Symptoms: "{user_symptoms}"

                Evaluation Rules:[Only necessary if the user ask you to identify his/her physical problems]
                1. Elevate Risk Level according to {user_age} and {symptom_days}
                2.the user might have multiple disease at once and you must strictly evaluate that.
                3. Co-relate symptoms with Pre-existing condition {existing_disease} based on {context_data}

                if the user's question is not relatable with  {context_data},then inform him about that with an apology and give some general health advice .
                Crucial: Always end with a medical disclaimer."""


                    try:
                        # Direct and strict initialization right before calling generating content
                        genai.configure(api_key=api_key)
                        model = genai.GenerativeModel(model_name="gemini-2.5-flash")
                        
                        response = model.generate_content(prompt, stream=True)
                        st.success("Answer from AI:")
                        st.write_stream(chunk.text for chunk in response)
                    except Exception as e:
                        st.error(f"Error connecting to AI: {e}")
    else:
        st.warning("Please enter a query.")

