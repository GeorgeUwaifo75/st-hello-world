import langchain_google_genai
from langchain_google_genai import ChatGoogleGenerativeAI

import google.generativeai as genai
from secret_key import GOOGLE_API_KEY

import os

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.7, google_api_key=GOOGLE_API_KEY)



def generate_restaurant_name_and_items(cuisine):
  return{
    "restaurant_name":"Curry Delight",
    "menu_items":"Samosa, paneer, tikka"
  }
