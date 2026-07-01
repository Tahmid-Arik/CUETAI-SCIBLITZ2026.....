 Health & Medical Care Assistant - SciBlitz 2026

An AI-powered clinical assistant application designed for the Health & Medical Track of Bangladesh. This application leverages the Google Gemini 2.5 Flash model with an optimized Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-bounded medical guidance based on a custom cardiovascular and pulmonary disease database.


 Features:

 Context-Bounded AI Analysis:Utilizing Gemini 2.5 Flash Lite to safely evaluate symptoms strictly within a verified medical database to prevent AI hallucination.
 Physical Metrics Engine: Integrated standalone Calculator for Body Mass Index (BMI) and Basal Metabolic Rate (BMR) utilizing the Mifflin-St Jeor Equation to adapt clinical guidance.
 Token-Optimized RAG/Filtering: Advanced context filtering mechanism that dynamically optimizes text databases to prevent token overflow (`429 Quota Exceeded`) and maximize API efficiency under strict Free Tier limitations.
Robust Error Handling: Built-in automatic retry mechanisms for mitigating temporary Google server demands (`503 Service Unavailable`).
Interactive UI: A highly responsive dashboard built entirely using Streamlit with strict state management and multi-column layouts.



  System Architecture & Optimization

Unlike traditional generic chatbots, this system implements a strict In-Context Learning (RAG) approach rather than static model fine-tuning. 

Core Optimization Strategy:
1. Dynamic Context-Filtering: The prompt evaluates user-specific inputs (`BMI`, `BMR`, `Age`, `Gender`) dynamically alongside the symptoms.
2. Token Management: Large knowledge bases are filtered to only pass highly relevant context chunks, dropping the context window token payload drastically, allowing seamless deployment under strict Google AI Studio API limits.



 Tech Stack:

Frontend & Dashboard:Streamlit
AI Engine:** Google Generative AI SDK (`gemini-2.5-flash-lite`)
Environment Management: Python-dotenv
Version Control & Hosting: Git, GitHub, Streamlit Cloud



 Project Structure:

text
 .env:Environment Variables (API Keys)
app.py:Main Streamlit Application Corerequirements.txt       Python Dependecies
 data:
disease_info.txt :Core Disease Knowledge Base & Evaluation Matrix
README.md: Project Documentation
