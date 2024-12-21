# PDF Question Answering App

## Overview

This is a PDF Question Answering web application built using **Streamlit**, **PyPDF2**, and the **Groq LLaMA-3** model. Users can upload a PDF document, ask questions related to the content of the PDF, and receive high-quality answers based on the document's text.

## Features

- **Upload PDF**: Users can upload text-based PDF files (up to 30,000 characters).
- **Ask Questions**: After uploading a PDF, users can ask questions based on the document's content.
- **Answer Generation**: The application processes the document and uses the LLaMA-3 model to generate answers based on the content.
- **Document Preview**: A preview of the uploaded document is shown to the user for context before asking questions.

## Requirements

To run this app locally, you'll need the following dependencies:

- **Python 3.x**
- **Streamlit**
- **PyPDF2**
- **Groq (for querying the LLaMA-3 model)**
- **python-dotenv** (for managing environment variables)

### Install the dependencies:

```bash
pip install streamlit PyPDF2 groq python-dotenv
