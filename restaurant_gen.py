import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("India", "Italian","Nigerian", "Ghanian", "American", "Mexican"))


if cuisine:
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)
  
  # Define keys explicitly
  restaurant_name_key = 'restaurant_name'
  menu_items_key = 'menu_items'

  st.header(response[restaurant_name_key].strip())
  menu_items = response[menu_items_key].strip().split(",")
  
  st.write("** Menu Items**")
  for item in menu_items:
    st.write("-",item)
