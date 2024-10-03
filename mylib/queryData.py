import sqlite3
import pandas as pd
from tabulate import tabulate

def logQuery(query):
    """adds to a query markdown file"""
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")

def queryData():
    """Query the database for the top 20 rows of the worker_health table"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM worker_health LIMIT 20")
    print("Top 20 rows of the worker_health table:")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description] # get headers
    for row in results:
        print(row)
    table = tabulate(results, headers=headers, tablefmt='pretty') # Create the table using tabulate
    print(table)
    connection.close()
    return "Success"

def querySpecificRecord(employee_id):
    """Query the database for a specific record based on Employee_ID"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM worker_health WHERE Employee_ID = ?", (employee_id,)) # Query for the specific employee
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

def createOrUpdateRecord(id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access):
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    
    # Attempt to insert a new record
    try:
        cursor.execute(
            """
            INSERT INTO worker_health 
            (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, Mental_Health_Condition, Access_to_Mental_Health_Resources) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access),)
    except sqlite3.IntegrityError:
        # If a UNIQUE constraint error occurs, update the existing record
        cursor.execute(
            """
            UPDATE worker_health SET 
            Age = ?, Job_Role = ?, Industry = ?, Years_of_Experience = ?, Work_Location = ?, 
            Hours_Worked_Per_Week = ?, Mental_Health_Condition = ?, Access_to_Mental_Health_Resources = ? 
            WHERE Employee_ID = ?
            """,
            (age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access, id),)
        
    connection.commit()
    connection.close()

    # Log the query in the md file
    logQuery(
        f"""INSERT INTO worker_health VALUES ({id}, {age}, {jobrole}, {industry}, {experience}, 
        {worklocation}, {hoursworked}, {mhcondition}, {access});""")
    
    return querySpecificRecord(id)

def deleteRecord(employee_id):
    """Delete a records from the worker_health table based on the EmployeeID"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM worker_health WHERE Employee_ID = ?", (employee_id,))
    connection.commit()
    connection.close()
    querySpecificRecord("EMP5000")
    return "Success"

# createOrUpdateRecord("EMP5000", 28, 'Data Analyst', 'Finance', 3, 'Onsite', 45, 'Anxiety', False)
# createOrUpdateRecord("EMP6000", 40, 'Data Scientist', 'IT', 15, 'Hybrid', 45, 'None', True)
# deleteRecord("EMP6000")