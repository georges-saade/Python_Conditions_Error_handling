import os
from lookups import error_handling

def get_all_csv(csv_folder):
    list_files=[]
    try:
        for x in os.listdir(csv_folder):
            if x.endswith(".csv"):
                list_files.append(x)
    except Exception as e:
        list_files=f"{error_handling.CSV_FILES_ERROR.value} - {str(e)}"
    return list_files


