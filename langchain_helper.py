import langchain_google_genai
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

# Initialize the Gemini model
#llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.7, google_api_key=GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.7)



def generate_restaurant_name_and_items(cuisine):
  return{
    "restaurant_name":"Curry Delight",
    "menu_items":"Samosa, paneer, tikka"
  }
