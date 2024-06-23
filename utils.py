import snowflake.connector as snowflake
from snowflake.connector import DictCursor
import pandas as pd
import os


def make_sql_query(table_names: list[str]) -> dict:
    """
    Carry out a SQL query, given a list of table names (provided by vector_query_engine_datalineage) as input to a SQL prompt
    that returns the data lineage SQL table, and return the results as a
    dictionary of DataFrames.

    Args:
        table_names (list of str): List of table names to query.

    Returns:
        dict: A dictionary with table names as keys and DataFrames as values.
    
    Given this output, answer question about the source systems (represented by column 'SRC_TABLE_NAME') 
    """
    # Connect to Snowflake
    con = snowflake.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        account=os.environ['account'],
        warehouse=os.environ['warehouse'],
        database=os.environ['database'],
    )
    
    # Dictionary to store the results
    result_dict = {}
    
    for table_name in table_names:
        query_template = f"""
            SELECT * 
            FROM EEE_RAG_PROJECT.METADATA.TABLE_LINEAGE_OLY 
            WHERE LVL0_TARGETNAME = '{table_name}'
        """
        cur = con.cursor(DictCursor)
        cur.execute(query_template)
        
        # Fetch the results and create a DataFrame
        rows = cur.fetchall()
        df_new = pd.DataFrame(rows)
        
        # Store the DataFrame in the dictionary
        result_dict[table_name] = df_new
        
        cur.close()
    
    # Close the connection
    con.close()
    
    return result_dict 

