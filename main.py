import streamlit as st
import pandas as pd

def copy_to_clipboard(text):
    df = pd.DataFrame({'text': [text]})
    df.to_clipboard(index=False, header=False)

st.markdown('<style>h1{font-family: Appetite;}</style>', unsafe_allow_html=True)
st.title("Copy Text App")
text = st.text_input("Enter text to copy")
if st.button("Copy"):
    if text != "":
        copy_to_clipboard(text)
        st.success("Text copied to clipboard!")
    else:
        st.error("Enter the text")