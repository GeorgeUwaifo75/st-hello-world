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
    prompt_template_name = PromptTemplate(
    input_variables=["cuisine"], 
    template="I want to open a restaurant for {cuisine} food. Can you suggest one fancy name?")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key ="restaurant" )

    prompt_template_items = PromptTemplate(
    input_variables=["restaurant"], 
    template="Suggest to me some food menu for the restaurant {restaurant}. Return it as a comma separate list.")

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key ="menu_items")

    chain = SequentialChain(
    chains=[name_chain, food_items_chain],
    input_variables=["cuisine"],
    output_variables=["restaurant", "menu_items"]
    )

    response = chain.revoke({"cuisine": cuisine})
    return response
