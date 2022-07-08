import acquire
import pandas as pd
import os

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




def get_q6_eda_df():
    '''This function converts the column types in the CSV from object to the correct type. Using the CSV cached locally results in dates saved as 'object; instead of datetimes'''
    
    df = prepare.prepare_logs()
    df.date_time = pd.to_datetime(df.date_time)
      # convert dates to DTG
    dates = ['start_date', 'end_date', 'created_at', 'updated_at']
    for col in dates:
        df[col] = pd.to_datetime(df[col])
        # drop unnecessary columns
    df = df.drop(columns=(['date', 'time']))
    return df