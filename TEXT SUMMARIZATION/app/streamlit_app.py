import streamlit as st
from transformers import pipeline

st.title("Text Summarization Tool")

text = st.text_area("Enter your text to summarize", height=300)

if st.button("Summarize"):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    st.subheader("Summary:")
    st.write(summary[0]['summary_text'])
