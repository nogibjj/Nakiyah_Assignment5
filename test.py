import subprocess

def createTest():
    result = subprocess.run(
        ["python3", "main.py", "create", 
         "EMP5000", "28", "Data Analyst", 
         "Finance", "3", "Onsite", "45",
         "Anxiety", "False"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Record with Employee_ID EMP5000" in result.stdout


createTest()
