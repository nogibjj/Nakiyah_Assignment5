import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os

def cleanData():
    df = pd.read_csv("Data/Impact_of_Remote_Work_on_Mental_Health.csv")
    print(df.columns)
    dfClean = df[['Employee_ID', 
                  'Age', 
                  'Job_Role', 
                  'Industry',
                  'Years_of_Experience', 
                  'Work_Location', 
                  'Hours_Worked_Per_Week', 'Mental_Health_Condition',
                  'Access_to_Mental_Health_Resources']].copy()

    # Convert Access_to_Mental_Health_Resources to boolean
    dfClean['Access_to_Mental_Health_Resources'] = dfClean['Access_to_Mental_Health_Resources'].map({'Yes': True, 'No': False})
    
    # Convert numeric columns to correct types and handle NaNs
    dfClean.loc[:, 'Age'] = pd.to_numeric(dfClean['Age'], errors='coerce')
    dfClean.loc[:, 'Years_of_Experience'] = pd.to_numeric(dfClean['Years_of_Experience'], errors='coerce')
    dfClean.loc[:, 'Hours_Worked_Per_Week'] = pd.to_numeric(dfClean['Hours_Worked_Per_Week'], errors='coerce')
    
    # Drop rows with NaN values
    dfClean.dropna(inplace=True)
    return dfClean


def loadData(data):
    "Transforms and Loads Data into SQL DB"

    # Load environment variables from .env file
    load_dotenv()
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS table1")
    create_table_query = """CREATE TABLE table1 (
    Employee_ID NUMERIC PRIMARY KEY,            
    Age INTEGER,                                
    Job_Role TEXT,                              
    Industry TEXT,                              
    Years_of_Experience INTEGER,                
    Work_Location TEXT,                         
    Hours_Worked_Per_Week INTEGER,              
    Mental_Health_Condition TEXT,               
    Access_to_Mental_Health_Resources BOOLEAN); """
    cursor.execute(create_table_query)
    # Insert
    cursor.executemany("INSERT INTO table1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data.values)
    connection.commit()
    connection.close()

    return "database1.db"



