import streamlit as st

st.title("Simple Text Processor")
text = st.text_area("Paste your text here")

if text:
    words = text.split()
    st.write(f"Word count: {len(words)}")
