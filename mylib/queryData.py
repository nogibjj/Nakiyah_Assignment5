import sqlite3
import pandas as pd
from tabulate import tabulate

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