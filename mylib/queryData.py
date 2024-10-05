import sqlite3
from tabulate import tabulate

# Markdown file to log the SQL functions and queries
def logQuery(query):
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")

# Query the top 20 records
def queryData(n): 
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM worker_health LIMIT {n}"
    cursor.execute(query)
    print(f"Top {n} rows of the worker_health table:")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description] # get headers
    # for row in results:
        # print(row)
    table = tabulate(results, headers=headers, tablefmt='pretty') # Create the table using tabulate
    print(table)
    connection.close()
    # Log the query in the md file
    logQuery(query)

# Query the database for a specific record based on Employee_ID
def querySpecificRecord(employee_id):
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
    # Log the query in the md file
    logQuery(f"SELECT * FROM worker_health WHERE Employee_ID = {employee_id}")

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
    logQuery(f"""INSERT INTO worker_health VALUES ({id}, {age}, {jobrole}, {industry}, {experience},
             {worklocation}, {hoursworked}, {mhcondition}, {access});""")
    
    # Print a success message including the Employee_ID
    print(f"Record with Employee_ID {id} created successfully.")
    return querySpecificRecord(id)
    
def deleteRecord(employee_id):
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM worker_health WHERE Employee_ID = ?", (employee_id,))
    connection.commit()
    connection.close()

    # Log the query in the md file
    logQuery(f"DELETE FROM worker_health WHERE Employee_ID = '{employee_id}';")
    return querySpecificRecord(employee_id)