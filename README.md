#PDF Question Answering App

## Introduction
PDF Question Answering is a web application developed by utilizing **Streamlit**, **PyPDF2**, and the **Groq LLaMA-3** model. Users can upload any PDF document, then pose questions related to it and get high-quality answers as a result of processing of text in the uploaded file.

## Features

Upload PDF. Users can upload text-based PDF files up to 30,000 characters long.
- **Ask Questions**: After uploading a PDF, users can ask questions based on the content of the document.
- **Answer Generation**: The application processes the document and uses the LLaMA-3 model to generate answers based on the content.
- **Document Preview**: A preview of the uploaded document is shown to the user for context before asking questions.

## Requirements

To run this app locally, you'll need the following dependencies:

- **Python 3.x**
- **Streamlit**
- **PyPDF2**
- **Groq (for querying the LLaMA-3 model)**
- **python-dotenv** (for managing environment variables)

### Install dependencies:

```bash
pip install streamlit PyPDF2 groq python-dotenv
```
