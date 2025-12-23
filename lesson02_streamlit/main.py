import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

st.title("Personal Chatbot")

language = st.text_input("Enter your language")
code_question = st.text_input("Enter your coding challenge question")

llm = ChatOllama(
    temperature=0,
    model="llama3.2:3b"
)

prompt_template = PromptTemplate(
    input_variables=["language", "code_question"],
    template="""
You are an expert in programming language {language}.
You provide optimized code for the coding question below in {language}.
If the question is not related to programming, reply that you are only an assistant for coding.

Question:
{code_question}
"""
)

if language and code_question:
    prompt_value = prompt_template.invoke({
        "language": language,
        "code_question": code_question
    })

    response = llm.invoke(prompt_value)

    st.write(response.content)
