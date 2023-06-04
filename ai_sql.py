from langchain.sql_database import SQLDatabase
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.prompts.prompt import PromptTemplate


st.title('sql Runner')
prompt = st.text_area('input command')

db_user = "docker"
db_password = "docker"
db_host = "lanchain_db"
db_name = "lanchain_test"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", verbose=True)
# llm = ChatOpenAI(model_name="gpt-4", verbose=True)

_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{table_info}

If someone asks for the table foobar, they really mean the employee table.

Question: {input}"""
PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
)
db_chain = SQLDatabaseChain.from_llm(llm, db, prompt=PROMPT, use_query_checker=False, verbose=True)


if prompt:
    answer = db_chain.run(prompt)

    st.write(answer)
