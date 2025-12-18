import streamlit as st

st.title("First project")
name = st.text_input("enter name: ")
if name:
  st.write(f"hello {name}")

age = st.text_input("enter age: ")
if age:
  st.write(f"your age is {age}")
