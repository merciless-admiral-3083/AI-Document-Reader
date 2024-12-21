import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("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"))

def query_llama3_model(document_text, question):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "The following document is provided for context. Please answer the user's question based on the content of the document."
                },
                {
                    "role": "assistant",
                    "content": document_text
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error querying LLAMA-3: {e}")
        return None

st.title("PDF Question Answering App")
st.write("Upload a PDF document and ask questions based on its content.")
st.sidebar.title("App Features")
st.sidebar.write("1. Upload a PDF file.")
st.sidebar.write("2. Ask questions based on its content.")
st.sidebar.write("3. Get high-quality answers!")

st.markdown("""
    <style>
    .stTextInput input {
        background-color: #f5f5f5;
        color: black;  /* Make the text black for better visibility */
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    footer {
        text-align: center;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.subheader("Upload a PDF File")
st.write("Please upload a text-based PDF file. Files should not exceed 30,000 characters.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

st.markdown("""
    <p style="color: grey; font-size: 12px;">Maximum file size: 30,000 characters. For larger files, consider splitting the document.</p>
""", unsafe_allow_html=True)

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    if len(text) > 30000:
        st.error("The document exceeds the 30,000 character limit. Please upload a smaller PDF.")
    else:
        st.subheader("Document Preview")
        with st.expander("Click to expand document preview"):
            st.write(text[:1000])  

        question = st.text_input("Ask a question based on the document:")

        submit_button = st.button("Submit Question")

        if submit_button and question:
            with st.spinner('Processing...'):
                answer = query_llama3_model(text, question)
            if answer:
                st.markdown(f"**Answer**: {answer}", unsafe_allow_html=True)

    

st.info("Upload a text-based PDF to get meaningful answers. For scanned PDFs, OCR might be needed.")
