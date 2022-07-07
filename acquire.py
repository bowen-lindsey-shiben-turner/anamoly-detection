#read only credentials
import pandas as pd
import numpy as np
from env import get_db_url
import os

def get_log_data():

    '''
    This function acquires curriculum log data by accessing a SQL database and performing a SQL query to acquire
    selected curriculum log tables and columns and return it to a dataframe. Additionally, data is stored in a .csv 
    making it more efficient for future utilization of the same function.
    '''

    filename = 'curriculum_logs.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        sql = """
        SELECT *
        FROM logs
        LEFT JOIN cohorts ON logs.cohort_id = cohorts.id
        """

        df = pd.read_sql(sql, get_db_url('curriculum_logs'))

        df.to_csv(filename)

        return df 