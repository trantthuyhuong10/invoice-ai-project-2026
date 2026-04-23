import streamlit as st
import requests

st.set_page_config(page_title="Invoice AI Chatbot")

st.title("💬 Invoice AI Chatbot")

# input
file_path = st.text_input("📄 File path:", "data/invoice1.pdf")
question = st.text_input("❓ Your question:")

# button
if st.button("Ask"):
    if not question:
        st.warning("Please enter a question")
    else:
        try:
            res = requests.post(
                "http://localhost:8000/chat",
                json={
                    "file_path": file_path,
                    "question": question
                }
            )

            result = res.json()

            st.success("✅ Answer:")
            st.write(result.get("answer"))

        except Exception as e:
            st.error(f"Error: {e}")