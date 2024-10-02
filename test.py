import subprocess
import os

# def createOrUpdateRecord(id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access):
#     connection = sqlite3.connect("database1.db")
#     cursor = connection.cursor()
    
#     # Attempt to insert a new record
#     try:
#         cursor.execute(
#             """
#             INSERT INTO table1 
#             (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, Mental_Health_Condition, Access_to_Mental_Health_Resources) 
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#             """,
#             (id, age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access),)
#     except sqlite3.IntegrityError:
#         # If a UNIQUE constraint error occurs, update the existing record
#         cursor.execute(
#             """
#             UPDATE table1 SET 
#             Age = ?, Job_Role = ?, Industry = ?, Years_of_Experience = ?, Work_Location = ?, 
#             Hours_Worked_Per_Week = ?, Mental_Health_Condition = ?, Access_to_Mental_Health_Resources = ? 
#             WHERE Employee_ID = ?
#             """,
#             (age, jobrole, industry, experience, worklocation, hoursworked, mhcondition, access, id),)
    
#     connection.commit()
#     connection.close()

def createTest():
    result = subprocess.run(["python3", "main.py", "create", "EMP5000", "28", 'Data Analyst', 'Finance', "3", 'Onsite', "45", 'Anxiety', "False"], 
                            capture_output=True, text=True, check=True)
    assert result.returncode == 0
    assert "Record with Employee_ID EMP5000" in result.stdout

createTest()

