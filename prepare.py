
# FUNCTIONS in this prepare.py:

# prepare_logs(): SQL query to obtain data, removes uneeded columns, creates CSV
# get_q6_eda(): converts DTG columns from strings to DTG types for EDA 
# wrangle_logs(): combines the two prior functions
# q2_df_prep(df): prepares a new dataframe for question 2

#______________________________________________________________________________________________________________________________________________________

import acquire
import pandas as pd
import os

#1._____________________________________________________________________________________________________________________________________________________

def prepare_logs(use_cache=True):
    """This function takes in the DataFrame from the get_log_data function located in the acquire file.
    Args: none. 
    Columns dropped: 'slack', 'id', and 'deleted_at'.
    Columns renamed: mapped values for program type to integers in 'program_id' column.
    Columns converted: 'start_date', 'end_date', 'created_at', 'updated_at' converted to DTG format.
    Columns concat: 'date' and 'time', converted to DTG
    Returns: prepared DF, and CSV named 'codeup_logs.csv'
      """
      #use local cache from CSV if available
    filename = "codeup_logs.csv"
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    # acquire the data
    df = df = acquire.get_log_data()
    # drop unnecessary columns
    df = df.drop(columns=(['slack', 'id', 'deleted_at', 'Unnamed: 0']))
    # map programs to program ids
    df.program_id = df.program_id.map({1.0:'full_stack_php', 
    2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    # convert dates to DTG
    dates = ['start_date', 'end_date', 'created_at', 'updated_at']
    for col in dates:
        df[col] = pd.to_datetime(df[col])
    # change cohort names to lower case
    df.name = df.name.str.lower()
    # convert date-time to DTG
    df['date_time'] = df.date + " " + df.time
    df.date_time = pd.to_datetime(df.date_time)
    # drop unnecessary columns
    df = df.drop(columns=(['date', 'time']))
    # add 'to_csv'
    df.to_csv(filename, index=False)
    return df


#2.______________________________________________________________________________________________________________________________________________________

def get_q6_eda_df():
    '''This function converts the column types in the CSV from object to the correct type. 
    Using the CSV cached locally results in dates saved as 'object; instead of datetimes'''

    df = prepare_logs()
    df.date_time = pd.to_datetime(df.date_time)
      # convert dates to DTG
    dates = ['start_date', 'end_date', 'created_at', 'updated_at']
    for col in dates:
        df[col] = pd.to_datetime(df[col])
        # drop unnecessary columns
    return df


#3.______________________________________________________________________________________________________________________________________________________

def wrangle_logs():
    df = prepare_logs()
    df = get_q6_eda_df()
    return df


#4.______________________________________________________________________________________________________________________________________________________

def q2_df_prep(df):
    '''
    Creates a new dataframe for question 2,
    "Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?"
    by adding a 'date_time' column with the concat of 'date' and 'time', dropping unnecessary columns of 'slack', 'id', 'deleted_at', 'Unnamed: 0', 'date', and 'time', dropping remaining rows with null values, remapping integer values under 'program_id' to word strings, converting columns with dates from object to timedate, making values in 'name' column lowercase, dropping 'staff' from 'names' column, and renaming 'name' and 'program_id' columns to 'cohort' and 'programs' respectively.
    '''
    
    # convert date-time to DTG
    df['date_time'] = df.date + " " + df.time
    
    # drop unnecessary columns
    df = df.drop(columns=(['slack', 'id', 'deleted_at', 'Unnamed: 0', 'date', 'time']))
    
    # Removes all rows from columns with null values
    df = df.dropna()
    
    # map programs to program ids
    df.program_id = df.program_id.map({1.0:'full_stack_php', 
    2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    
    # convert dates to DTG
    dates = ['start_date', 'end_date', 'created_at', 'updated_at', 'date_time']
    for col in dates:
        df[col] = pd.to_datetime(df[col])
    
    # change cohort names to lower case
    df.name = df.name.str.lower()
    
    # Drops rows with value 'staff' under the 'name' column 
    df = df[(df['name'] != 'staff')]
    
    # Renames specified columns
    df2 = df.copy()
    df2 = df2.rename(columns={'name': 'cohort', 'program_id': 'programs'})
    return df2