import streamlit as st

st.set_page_config(page_title="Weatherly", layout="centered")


with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.components.v1.html(html_content, height=800, scrolling=True)
