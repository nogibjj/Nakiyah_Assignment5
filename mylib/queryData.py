import sqlite3
import pandas as pd
from tabulate import tabulate

# Define a global variable for the log file
logFile = "queryLog.md"

def queryData():
    """Query the database for the top 20 rows of the table1 table"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM table1 LIMIT 20")

    print("Top 20 rows of the table1 table:")
    results = cursor.fetchall()
    # get headers
    headers = [description[0] for description in cursor.description]

    # Print each row
    for row in results:
        print(row)

    # Create the table using tabulate
    table = tabulate(results, headers=headers, tablefmt='pretty')

    # Print the table
    print(table)
    connection.close()

    return "Success"

def querySpecificRecord(employee_id):
    """Query the database for a specific record based on Employee_ID"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    
    # Query for the specific employee
    query = cursor.execute("SELECT * FROM table1 WHERE Employee_ID = ?", (employee_id,))
    
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    
    # If the record exists, print it
    if results:
        print(f"Record with Employee_ID {employee_id}:")
        table = tabulate(results, headers=headers, tablefmt='pretty')
        print(table)
    else:
        print(f"No record found for Employee_ID {employee_id}")
    
    connection.close()


def logQuery(query):
    """adds to a query markdown file"""
    with open(logFile, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


# def createRecord(id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access):

#     connection = sqlite3.connect("database1.db")
#     cursor = connection.cursor()

#     cursor.execute(
#     """
#     INSERT INTO table1 
#     (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, Mental_Health_Condition, Access_to_Mental_Health_Resources) 
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """,
#     (id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access),)
#     connection.commit()
#     connection.close()

def createOrUpdateRecord(id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access):
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    
    # Attempt to insert a new record
    try:
        cursor.execute(
            """
            INSERT INTO table1 
            (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, Mental_Health_Condition, Access_to_Mental_Health_Resources) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access),)
    except sqlite3.IntegrityError:
        # If a UNIQUE constraint error occurs, update the existing record
        cursor.execute(
            """
            UPDATE table1 SET 
            Age = ?, Job_Role = ?, Industry = ?, Years_of_Experience = ?, Work_Location = ?, 
            Hours_Worked_Per_Week = ?, Mental_Health_Condition = ?, Access_to_Mental_Health_Resources = ? 
            WHERE Employee_ID = ?
            """,
            (age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access, id),)
    
    connection.commit()
    connection.close()


    # Log the query
    logQuery(
        f"""INSERT INTO table1 VALUES (
            {id}, 
            {age}, 
            {jobrole}, 
            {industry}, 
            {experience}, 
            {worklocation}, 
            {hoursworked},
            {mhcondition},
            {access});"""
    )


createOrUpdateRecord("EMP5000", 28, 'Data Analyst', 'Finance', 3, 'Onsite', 45, 'Anxiety', False)
# Query to see if the record was added
querySpecificRecord("EMP5000")