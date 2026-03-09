import streamlit as st import pandas as pd
st.title("Лобими неша класна анкета")
if "colors" not in st.session_state:
st.session_state.colors = {
"Червен": 0,
"Син": 0,
"Зелен": 0,
"Жълт": 0
}
if "sports" not in st.session_state:
st.session_state.sports = {
"Футбол": 0,
"Баскетбол": 0,
"Волейбол": 0,
"Плуване": 0
}
st.subheader("Избери любими неща")
color
=
st.selectbox("Лбим Übят:", list(st.session_state.colors.keys())) sport st.selectbox("Лнбим спорт:", list(st.session_state.sports.keys()))
