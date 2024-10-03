import pandas as pd
import sqlite3

def logQuery(query):
    """adds to a query markdown file"""
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")

def cleanData():
    df = pd.read_csv("Data/Impact_of_Remote_Work_on_Mental_Health.csv")
    print(df.columns)
    dfClean = df[['Employee_ID', 'Age', 'Job_Role', 
                  'Industry', 'Years_of_Experience', 'Work_Location', 
                  'Hours_Worked_Per_Week', 'Mental_Health_Condition',
                  'Access_to_Mental_Health_Resources']].copy()

    # Converting Access_to_Mental_Health_Resources to boolean
    dfClean['Access_to_Mental_Health_Resources'] = dfClean['Access_to_Mental_Health_Resources'].map({'Yes': True, 'No': False})
    dfClean.loc[:, 'Age'] = pd.to_numeric(dfClean['Age'], errors='coerce')
    dfClean.loc[:, 'Years_of_Experience'] = pd.to_numeric(dfClean['Years_of_Experience'], errors='coerce')
    dfClean.loc[:, 'Hours_Worked_Per_Week'] = pd.to_numeric(dfClean['Hours_Worked_Per_Week'], errors='coerce')
    dfClean.dropna(inplace=True)
    return dfClean

def loadData(data):
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS worker_health")
    createTableQuery = """CREATE TABLE worker_health (
    Employee_ID NUMERIC PRIMARY KEY,            
    Age INTEGER,                                
    Job_Role TEXT,                              
    Industry TEXT,                              
    Years_of_Experience INTEGER,                
    Work_Location TEXT,                         
    Hours_Worked_Per_Week INTEGER,              
    Mental_Health_Condition TEXT,               
    Access_to_Mental_Health_Resources BOOLEAN); """
    cursor.execute(createTableQuery)

    # Insert
    insertQuery = "INSERT INTO worker_health VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(insertQuery, data.values)
    connection.commit()
    connection.close()

    # Log each row in the data for better tracking
    logQuery("""CREATE TABLE worker_health (
    Employee_ID NUMERIC PRIMARY KEY,            
    Age INTEGER,                                
    Job_Role TEXT,                              
    Industry TEXT,                              
    Years_of_Experience INTEGER,                
    Work_Location TEXT,                         
    Hours_Worked_Per_Week INTEGER,              
    Mental_Health_Condition TEXT,               
    Access_to_Mental_Health_Resources BOOLEAN);""")

    logQuery(f"Inserted {len(data)} rows from the CSV file into the worker_health table.")