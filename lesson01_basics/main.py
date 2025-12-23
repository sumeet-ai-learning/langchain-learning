import os

from colorama.initialise import reset_all
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st
load_dotenv(override=True)

if __name__ == '__main__':
    print('PyCharm')
    print(os.environ.get('OPENAI_API_KEY'))

    information = """Elon Reeve Musk (born June 28, 1971) is an engineer, entrepreneur, and business magnate. He holds South African citizenship by birth, Canadian citizenship through his mother, and became a U.S. citizen in 2002.[1][2][3][4]
Musk holds leadership roles at Tesla, which develops electric vehicles, battery energy storage, and autonomous driving technologies; SpaceX, which develops reusable rockets and satellite internet constellations; and xAI and X, focused on artificial intelligence and digital platforms.[5][6][7] His early ventures include co-founding Zip2, an online business directory sold to Compaq in 1999, and X.com, which merged into PayPal and was acquired by eBay in 2002.[8][9] He founded Neuralink in 2016 to develop brain-machine interfaces and [The Boring Company](/The Boring Company) in 2016 for urban tunneling projects.[10][11][12]
As of December 2025, Forbes estimates Musk's net worth at over $600 billion, derived primarily from his stakes in Tesla, SpaceX, and xAI, positioning him among the wealthiest individuals.[13][14] His public profile includes advocacy for innovation, population growth, reduced government intervention, and free speech, as well as political involvement."""
    summary_template = f"""
    given the information {information} about a person I want you to create
    1. A short summary
    2. two interesting points
"""
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    #print(information)

    llm = ChatOllama(temperature=0,model="gemma3:4b")
    chain = summary_prompt_template|llm
    response = chain.invoke(input={"information":information})
    print(response.content)
