from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
import streamlit as st

st.title('sql Runner')
prompt = st.text_area('input command')

db_user = "docker"
db_password = "docker"
db_host = "lanchain_db"
db_name = "lanchain_test"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", verbose=True)
llm = ChatOpenAI(model_name="gpt-4", verbose=True)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


if prompt:
    answer = db_chain.run(prompt)

    st.write(answer)
