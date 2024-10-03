import subprocess


def testExtract():
    result = subprocess.run(
        ["python3", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Stdout (Extract):", result.stdout)
    print("Stderr (Extract):", result.stderr)
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def testLoad():
    result = subprocess.run(
        ["python3", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Stdout (Load):", result.stdout)  # Debug output
    print("Stderr (Load):", result.stderr)  # Debug output
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def testQuery():
    result = subprocess.run(
        ["python3", "main.py", "query"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Top 20 rows of the worker_health table:" in result.stdout


def testCreate():
    # First record
    result1 = subprocess.run(
        [
            "python3",
            "main.py",
            "create",
            "EMP5000",
            "28",
            "Data Analyst",
            "Finance",
            "3",
            "Onsite",
            "45",
            "Anxiety",
            "False",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Create Output 1:", result1.stdout)  # Debugging line
    assert result1.returncode == 0
    assert "Record with Employee_ID EMP5000" in result1.stdout

    # Second record
    result2 = subprocess.run(
        [
            "python3",
            "main.py",
            "create",
            "EMP6000",
            "40",
            "Data Scientist",
            "IT",
            "15",
            "Hybrid",
            "40",
            "None",
            "True",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Create Output 2:", result2.stdout)  # Debugging line
    assert result2.returncode == 0
    assert "Record with Employee_ID EMP6000" in result2.stdout

def testDelete():
    result = subprocess.run(
        ["python3", "main.py", "delete", "EMP5000"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Deleting selected query..." in result.stdout

if __name__ == "__main__":
    testExtract()
    testLoad()
    testQuery()
    testCreate()
    testDelete()
