import psycopg2
import pandas as pd
from lookups import error_handling
from lookups import file_types

db_name='dvdrental'
db_user='postgres'
db_password='admin'
db_host='localhost'
db_port=5432

def create_connection():
    db_session=None
    try:
        db_session=psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
    except Exception as e:
        db_session=f"{error_handling.CON_ERROR.value} - {str(e)}"
    finally:
        return db_session

def close_connection(db_session):
    try:
        db_session.close()
    except Exception as e:
        print(f"{error_handling.CON_CLOSE_ERROR.value} - {str(e)}")

def return_query(db_session,query):
    result=None
    try:
        cursor=db_session.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        db_session.commit()
    except Exception as e:
        result=f"{error_handling.RETURN_QUERY_ERROR.value} - {str(e)}"
    finally:
        return result
    
def return_data_as_df(db_session,file_executor,file_type):
    return_df=None
    try:
        if file_type==file_types.SQL:
            return_df=pd.read_sql_query(con=db_session,sql=file_executor)
        elif file_type==file_types.CSV:
            return_df=pd.read_csv(file_executor)
        elif file_type==file_types.EXCEL:
            return_df=pd.read_excel(file_executor)
        else:
            raise Exception("Undefined file type")
    except Exception as e:
        if file_type==file_types.SQL:
            return_df=f"{error_handling.RETURN_SQL_ERROR.value} - {str(e)}"
        elif file_type==file_types.CSV:
            return_df=f"{error_handling.RETURN_CSV_ERROR.value} - {str(e)}"
        elif file_type==file_types.EXCEL:
            return_df=f"{error_handling.RETURN_EXCEL_ERROR.value} - {str(e)}"
    finally:
        return return_df


def execute_query(db_session,query):
    result=error_handling.QUERY_EXECUTION_SUCCESS
    try:
        cursor=db_session.cursor()
        cursor.execute(query)
        db_session.commit()
    except Exception as e:
        result=f"{error_handling.QUERY_EXECUTION_ERROR.value} - {str(e)}"
    finally:
        return result
    
def get_schema_information(db_session,schema_name):
    return_result=None
    try:
        query=f"""
        SELECT
        *
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA='{schema_name}'
        """
        return_result=return_query(db_session=db_session,query=query)
        return return_result
    except Exception as e:
        return_result=f"{error_handling.SCHEMA_INFORMATION_ERROR.value} - {str(e)}"
    finally:
        return return_result
    

    


    


            



