import streamlit as st
import langchain_helper


st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian","Nigerian", "Ghanian", "American", "Mexican"))


if cuisine:
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)
 
  
  # Define keys explicitly
  restaurant_name_key = 'restaurant'
  menu_items_key = 'menu_items'

  st.header(response[restaurant_name_key])
  menu_items = response[menu_items_key].split(",")

  
  
  st.write("** Menu Items**")
  for item in menu_items:
    st.write("-",item)
