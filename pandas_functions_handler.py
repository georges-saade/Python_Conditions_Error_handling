import pandas as pd
from lookups import error_handling,function_types


def pandas_functions(dataframe,function_type):
    return_df=None
    try:
        if function_type==function_types.REMOVE_DUPLICATES:
            return_df=dataframe.drop_duplicates()
        elif function_type==function_types.REMOVE_NULLS:
             return_df=dataframe.dropna()
        elif function_type==function_types.GET_SHAPE:
            return_df=dataframe.shape
        elif function_type==function_types.GET_LENGTH:
            return_df=dataframe.size
        elif function_type==function_types.GET_BLANKS:
            return_df=dataframe.loc[dataframe.isnull().any(axis=1)]
        else:
            raise Exception("Undefined function type")
    except Exception as e:
        if function_type==function_types.REMOVE_DUPLICATES:
            return_df=f"{error_handling.REMOVE_DUPLICATES_ERROR.value} - {str(e)}"
        elif function_type==function_types.REMOVE_NULLS:
            return_df=f"{error_handling.REMOVE_NULLS_ERROR.value} - {str(e)}"
        elif function_type==function_types.GET_SHAPE:
            return_df=f"{error_handling.GET_SHAPE_ERROR.value} - {str(e)}"
        elif function_type==function_types.GET_LENGTH:
            return_df=f"{error_handling.GET_LENGTH_ERROR.value} - {str(e)}"
        elif function_type==function_types.GET_BLANKS:
            return_df=f"{error_handling.GET_BLANK_ERROR.value} - {str(e)}"
    finally:
        return return_df