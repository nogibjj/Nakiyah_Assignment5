# Nakiyah_Assignment5

[![cicd](https://github.com/nogibjj/Nakiyah_Assignment5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_Assignment5/actions/workflows/cicd.yml)

```
Nakiyah_Assignment5/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── Data/
│   └── Impact_of_Remote_Work_on_Mental_Health.csv
├── mylib/
│   ├── extractData.py
│   ├── loadData.py
│   └── queryData.py
├── main.py
├── test.py
├── Makefile
├── README.md
├── Requirements.txt
├── database1.db
├── testOutputs.md
└── queryLog.md

```
## Purpose of this project

### Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline that processes data from external public datasets and stores it in a SQLite database. The key stages of the pipeline are as follows:

Extract: 
Data is fetched from a public GitHub repository and loaded into a local CSV file.

Transform & Load: 
The CSV file is cleaned and pre-processed, ensuring the data is structured correctly and ready for analysis. The cleaned data is then loaded into a SQLite .db file, where it can be efficiently queried for further analysis.

Querying: Verifies that SQL queries, such as retrieving the top 20 rows from a specific table, return the expected results.
Testing:
To ensure the robustness of the ETL process, a suite of unit tests are executed using Python's subprocess module to simulate the full pipeline, testing each stage and validating the CRUD (Create, Read, Update, Delete) operations.

### Sample CRUD operations

Create using createRecord() --> This function creates a new record in the worker_health table
```python
python3 main.py create "EMP90005" 28 "Data Analyst" "Finance" 3 "Onsite" 45 "Anxiety" False 
python3 main.py create "EMP90006" 40 "Data Scientist" "IT" 15 "Hybrid" 40 "None" True
```


Read using queryData(n) --> This function retrieves the top n records from the worker_health table
```python
python3 main.py query
```


Update using updateRecord() --> This function updates an existing record in the worker_health table
```python
python3 main.py update "EMP90005", 28, "Software Engineer", "Tech", 3, "Onsite", 45, "Anxiety", False 
```

Delete using deleteRecord() --> This function deletes a record from the worker_health table based on Employee ID
```python
python3 main.py delete "EMP90006"
```