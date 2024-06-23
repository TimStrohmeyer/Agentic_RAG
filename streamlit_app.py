import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.tools import QueryEngineTool, BaseTool, FunctionTool, ToolMetadata
from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector, LLMMultiSelector
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.selectors import PydanticMultiSelector, PydanticSingleSelector
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
import snowflake.connector as snowflake
from snowflake.connector import DictCursor
import pandas as pd
from dotenv import load_dotenv
import os
from utils import make_sql_query

# Load environment variables
dotenv_path = 'KEYs.env'
_ = load_dotenv(dotenv_path)

# Initialize Pinecone
pc = Pinecone(api_key="0b599dcc-57d9-4d1a-8c46-d245c8d1a7ec")

# Initialize your index 
wiki_index = pc.Index("internalrag-mini-wiki")
datalineage_index = pc.Index("internalrag-mini-datalineage")

# Initialize VectorStore
vector_store_wiki = PineconeVectorStore(pinecone_index=wiki_index)
vector_store_datalineage = PineconeVectorStore(pinecone_index=datalineage_index)

# Instantiate VectorStoreIndex object from your vector_store object
vector_index_wiki = VectorStoreIndex.from_vector_store(vector_store=vector_store_wiki)
vector_index_datalineage = VectorStoreIndex.from_vector_store(vector_store=vector_store_datalineage)

# Streamlit UI
st.title("Reeeliance QA Tool")
st.write("Ask your questions below:")

# User input
user_query = st.text_input("Your question:", "")

if user_query:
    # Your existing chatbot logic here
    # Query Engines
    vector_query_engine_wiki = vector_index_wiki.as_query_engine()
    vector_query_engine_datalineage = vector_index_datalineage.as_query_engine()

    # Create Query Engine Tool
    vector_tool_wiki = QueryEngineTool.from_defaults(
        query_engine=vector_query_engine_wiki,
        description=(
            "Useful for retrieving specific context from wiki entries and naming conventions"
        ),
    )

    vector_tool_datalineage = QueryEngineTool.from_defaults(
        query_engine=vector_query_engine_datalineage,
        description=(
            "Useful only to answer questions regarding the source systems for specific tables (e.g. What are the source systems for table x, where does the information for table x come from, etc.)." 
            "the output of this query engine are NOT the final source systems, but only the correct Table Name(s) (i.e. LVL0_TargetName from the data catalogue). The correct LVL0_TargetName(s) by finding the most fitting table descriptions, based on the table name or description given in the user query."
        ),
    )

    # Define Router Query Engine
    query_engine = RouterQueryEngine(
        selector=PydanticSingleSelector.from_defaults(),
        query_engine_tools=[
            vector_tool_wiki,
            vector_tool_datalineage,
        ],
        verbose=True
    )

    response = query_engine.query(user_query)

    if response.metadata['selector_result'].selections[0].index == 1: 
        sql_query_tool = FunctionTool.from_defaults(fn=make_sql_query)

        llm = OpenAI(model="gpt-4-1106-preview", temperature=0)
        agent = ReActAgent.from_tools([sql_query_tool], llm=llm, verbose=True)

        final_response_template = f"""Given these preliminary table names provided in the following reponse, perform make_sql_query and answer question regarding the source systems: 
                                    ---
                                    Previous Response: {response}
                                    ---
                                    SQL TABLE LEGEND: 
                                    LvL0_TargetName: Name of the target table in the Data Mart and Curated Zone
                                    DV_Physical_Schema: Name of the Schema for the Vault and Standardized Zone
                                    DV_Table_Name: Name of the Table or Vault object in the Vault and Standardized Zone
                                    SRC_Physical_Schema: Name of the Schema for the Raw Zone table, containing the source systems
                                    SRC_Table_Name: Name of the Table in the Raw Zone, containing the table name in the respective source systems
                                    """
        response_final = agent.chat(final_response_template)
        
        st.write(str(response_final))
    else:
        st.write(str(response))