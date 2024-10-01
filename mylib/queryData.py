import sqlite3


def queryData():
    """Query the database for the top 20 rows of the table1 table"""
    connection = sqlite3.connect("database1.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table1")

    print("Top 20 rows of the table1 table:")
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()
    return "Success"