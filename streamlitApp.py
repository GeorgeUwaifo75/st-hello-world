import streamlit as st

st.title('My First Streamlit App')
st.write('Hello my friend!')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)
