import subprocess
import os

def testExtract():
    """tests extract()"""
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
    """tests the load() function"""
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

# def testCreate():
#     # First record
#     result1 = subprocess.run(
#         ["python3", "main.py", "create",
#          "EMP5000", "28", "Data Analyst",
#          "Finance", "3", "Onsite",
#          "45", "Anxiety", "False"],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     print("Create Output 1:", result1.stdout)  # Debugging line
#     assert result1.returncode == 0
#     assert "Record with Employee_ID EMP5000" in result1.stdout


