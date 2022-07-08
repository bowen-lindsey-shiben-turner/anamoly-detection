import acquire
import prepare
import pandas as pd
import os


def explore_question3(df):
    '''
    This function creates a dataframe tailored to explore the following:
    
    Question 3:
    Are there students who, when active, hardly access the curriculum? 
    If so, what information do you have about these students?

    The function renames columns & drops records that are not associated with 
    active students.
    '''
    df3 = df.copy()
    df3 = df3.rename(columns={'program_id': 'program', 'name': 'cohort'})
    #rename columns just for preference
    df3 = df3.dropna()
    #drops nulls, records without sufficient data about student access
    df3['program_access'] = (df3.date_time >= df3.start_date) & (df3.date_time <= df3.end_date)
    # creates boolean column to weed out everything, but active students
    df3 = df3[(df3['program_access'] == True)]
    df3 = df3[(df3['cohort'] != 'staff')] 
    #creates df of active students that are not staff
    df3[['date_time', 'start_date', 'end_date', 'created_at', 'updated_at']] = df3[['date_time','start_date', 'end_date', 'created_at', 'updated_at']].apply(pd.to_datetime)
    #converts selected columns to datetime format
    df3 = df3.drop(columns=['cohort_id'])
    #drops unnecessary column
    df3['user_id'] = df3['user_id'].astype(object)

    return df3