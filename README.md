# PDFs Analyzer – Streamlit LLM UI

This is a Streamlit-based web interface that allows users to interact with a language model (LLM) by submitting a message and optionally uploading PDF documents. The application extracts text from the uploaded PDFs, appends it to the user's prompt, and sends the combined input to an API endpoint.


## Features

- Accepts one or more PDF files as input
- Extracts and cleans text from each PDF
- Appends extracted text to the user’s message
- Sends the combined message to a language model backend API
- Maintains session-based chat history
- Supports both plain text and structured responses


## Installation
### 1. Clone the repository
### 2.Install dependencies

pip install -r requirements.txt

### 3.Use ui

In the Python code, update the API_URL variable with the address of your own API endpoint. 

to run the code: streamlit run app.py

Enter your prompt or message in the text box.

Optionally upload one or more PDF files.

Click the "Send" button.

The app will extract and clean the text from the PDFs, append it to your message, and send everything to the configured API.

The assistant’s response will be shown below and stored in the session chat history.

