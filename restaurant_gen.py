import streamlit as st
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("India", "Italian","Nigerian", "Ghanian", "American", "Mexican"))

def generate_restaurant_name_and_items(cuisine):
  return{
    "restaurant_name":"Curry Delight",
    "menu_items":"Samosa, paneer, tikka"
  }

if cuisine:
  response = generate_restaurant_name_and_items(cuisine)
  st.header(response[restaurant_name])
  menu_items = response[menu_items].split(",")
  
  st.write("** Menu Items**")
  for item in menu_items:
    st.write("-",item)
