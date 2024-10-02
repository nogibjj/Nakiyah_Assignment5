import subprocess

def testCreate():
    # First record
    result1 = subprocess.run(
        ["python3", "main.py", "create", 
        "EMP5000", "28", "Data Analyst", 
        "Finance", "3", "Onsite", "45",
        "Anxiety", "False"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result1.returncode == 0
    assert "Record with Employee_ID EMP5000" in result1.stdout

    # Second record
    result2 = subprocess.run(
        ["python3", "main.py", "create", 
        "EMP6000", "40", "Data Scientist", 
        "IT", "15", "Hybrid", "40",
        "None", "True"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result2.returncode == 0
    assert "Record with Employee_ID EMP6000" in result2.stdout

def testDelete():
    """tests the delete() function"""
    result = subprocess.run(
        ["python3", "main.py", "delete", "EMP6000"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Delete Record" in result.stdout


if __name__=="__main__":
    testCreate()
    testDelete()
