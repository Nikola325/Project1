import streamlit as st

st.title("First project")
name = st.text_input("enter name:")
if name:
  st.write(f"hello{name}")r
