from enum import Enum

class error_handling(Enum):
    CON_ERROR="DB Connection Error"
    RETURN_QUERY_ERROR="Error returning query"
    QUERY_EXECUTION_ERROR="Error executing query"
    QUERY_EXECUTION_SUCCESS="Query successfully executed"
    RETURN_SQL_ERROR="Error returning SQL as dataframe"
    RETURN_CSV_ERROR="Error returning CSV as dataframe"
    RETURN_EXCEL_ERROR="Error returning Excel as dataframe"
    SCHEMA_INFORMATION_ERROR="Error getting schema information"
    REMOVE_DUPLICATES_ERROR="Error removing duplicates from dataframe"
    CSV_FILES_ERROR="Error return csv files"
    REMOVE_NULLS_ERROR="Error removing nulls from dataframe"
    GET_SHAPE_ERROR="Error returning shape from dataframe"
    GET_LENGTH_ERROR="Error returning length from dataframe"
    GET_BLANK_ERROR="Error returning blanks from dataframe"
    CON_CLOSE_ERROR="DB closing connection error"
    
class file_types(Enum):
    SQL="SQL"
    EXCEL="Excel"
    CSV="CSV"


