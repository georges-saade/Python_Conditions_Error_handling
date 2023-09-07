import pandas as pd
from lookups import error_handling


def remove_duplicates(dataframe):
    return_df=None
    try:
        return_df=dataframe.drop_duplicates()
    except Exception as e:
        return_df=f"{error_handling.REMOVE_DUPLICATES_ERROR.value} - {str(e)}"
    finally:
        return return_df


def remove_nulls(dataframe):
    return_df=None
    try:
        return_df=dataframe.dropna()
    except Exception as e:
        return_df=f"{error_handling.REMOVE_NULLS_ERROR.value} - {str(e)}"
    finally:
        return return_df


def get_shape(dataframe):
    return_df=None
    try:
        return_df=dataframe.shape
    except Exception as e:
        return_df=f"{error_handling.GET_SHAPE_ERROR.value} - {str(e)}"
    finally:
        return return_df

def get_length(dataframe):
    return_df=None
    try:
        return_df=dataframe.size
    except Exception as e:
        return_df=f"{error_handling.GET_LENGTH_ERROR.value} - {str(e)}"
    finally:
        return return_df
    
def get_blanks(dataframe):
    return_df=None
    try:
       return_df=dataframe.loc[dataframe.isnull().any(axis=1)]
    except Exception as e:
        return_df=f"{error_handling.GET_BLANK_ERROR.value} - {str(e)}"
    finally:
        return return_df