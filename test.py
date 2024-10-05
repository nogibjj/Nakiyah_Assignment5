import subprocess
import os

def writeToMD(content):
    with open("testOutputs.md", "a") as f:
        f.write(content + "\n\n")


def logOutput(result, description):
    writeToMD(f"### {description}")
    writeToMD(f"**Command:** `{ ' '.join(result.args) }`")
    writeToMD(f"**Return code:** {result.returncode}")
    
    # Log STDOUT if available
    stdout_output = result.stdout if result.stdout else "(No output)"
    writeToMD(f"**STDOUT:**\n```plaintext\n{stdout_output}\n```")
    
    # Log STDERR if available
    stderr_output = result.stderr if result.stderr else "(No error output)"
    writeToMD(f"**STDERR:**\n```plaintext\n{stderr_output}\n```")


def testExtract():
    result = subprocess.run(
        ["python3", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Stdout (Extract):", result.stdout)
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout

def testLoad():
    result = subprocess.run(
        ["python3", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Stdout (Load):", result.stdout)
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def testQuery():
    result = subprocess.run(
        ["python3", "main.py", "query"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Stdout (Query):", result.stdout)
    assert result.returncode == 0
    assert "Top 20 rows of the worker_health table:" in result.stdout
    logOutput(result, "Top 20 Record")


def testCreate():
    # First record
    result1 = subprocess.run(
        ["python3", "main.py", "create",
         "EMP5000", "28", "Data Analyst", 
         "Finance", "3", "Onsite",
         "45", "Anxiety", "False"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Create Output 1:", result1.stdout)
    assert result1.returncode == 0
    assert "Record with Employee_ID EMP5000" in result1.stdout
    logOutput(result1, "Add Record 1")

    # Second record
    result2 = subprocess.run(
        ["python3", "main.py", "create",
         "EMP6000", "40", "Data Scientist",
         "IT", "15", "Hybrid",
         "40", "None", "True"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Create Output 2:", result2.stdout)
    assert result2.returncode == 0
    assert "Record with Employee_ID EMP6000" in result2.stdout
    logOutput(result2, "Add Record 2")


def testDelete():
    result = subprocess.run(
        ["python3", "main.py", "delete", "EMP6000"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Delete specific query:", result.stdout)
    assert result.returncode == 0
    assert "Deleting selected query..." in result.stdout
    logOutput(result, "Delete Record")

if __name__ == "__main__":

    # Clear the existing .md file if it exists
    if os.path.exists("testOutputs.md"):
        os.remove("testOutputs.md")
   
    if os.path.exists("queryLog.md"):
        os.remove("queryLog.md")

        
    testExtract()
    testLoad()
    testQuery()
    testCreate()
    testDelete()
