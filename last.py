import streamlit as st
import requests
import fitz  # PyMuPDF

st.title("🧠 PDFs Analyzer")

API_URL = "https://b04e-34-143-238-169.ngrok-free.app"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "submitted_once" not in st.session_state:
    st.session_state.submitted_once = False

# Display previous chat messages
for msg in st.session_state.messages:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Assistant"
    if isinstance(msg["content"], dict):
        st.markdown(f"**{role}:**")
        st.json(msg["content"])
    else:
        st.markdown(f"**{role}:** {msg['content']}")

# Chat form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("Type your message:")
    uploaded_files = st.file_uploader(
        "Upload one or more PDFs (optional)",
        type=["pdf"],
        accept_multiple_files=True
    )
    submitted = st.form_submit_button("Send")

# Handle form submission
if submitted and user_input.strip() and not st.session_state.submitted_once:
    pdf_content = ""

    # Extract text from uploaded PDFs
    if uploaded_files:
        for uploaded_file in uploaded_files:
            pdf_bytes = uploaded_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

            pdf_text = ""
            for page in pdf_document:
                pdf_text += page.get_text() + "\n"

            cleaned_text = "\n".join([line.strip() for line in pdf_text.splitlines() if line.strip()])
            pdf_content += f"\n\n=== Content from {uploaded_file.name} ===\n\n{cleaned_text}"

    # Combine user input and extracted text
    combined_message = user_input.strip() + ("\n\n" + pdf_content if pdf_content else "")

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    # Send to API and get response
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL + "/chat", json={"message": combined_message})
            if response.status_code == 200:
                bot_reply = response.json().get("response", {})
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                st.session_state.submitted_once = True
                st.rerun()  # rerun to show the new assistant message
            else:
                st.error("❌ Failed to reach the model.")
        except Exception as e:
            st.error("❌ Request failed: " + str(e))

# Reset flag on rerun so form can be used again
elif st.session_state.submitted_once:
    st.session_state.submitted_once = False

# Handle edge cases
elif submitted and uploaded_files and not user_input.strip():
    st.warning("Please include a message explaining what you want me to do with the PDF(s).")
elif submitted and not user_input.strip():
    st.warning("Please type a message or upload a PDF with instructions.")
