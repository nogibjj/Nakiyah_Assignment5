# Nakiyah_Assignment5

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

Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline that processes data from external public datasets and stores it in a SQLite database. The key stages of the pipeline are as follows:

Extract: Data is fetched from a public GitHub repository and loaded into a local CSV file.
Transform & Load: The CSV file is cleaned and pre-processed, ensuring the data is structured correctly and ready for analysis. The cleaned data is then loaded into a SQLite .db file, where it can be efficiently queried for further analysis.

Querying: Verifies that SQL queries, such as retrieving the top 20 rows from a specific table, return the expected results.

Query & Unit Testing 
To ensure the robustness of the ETL process, a suite of unit tests is included. These tests are executed using Python's subprocess module to simulate the full pipeline, testing each stage for correctness. The tests validate the following:

Create using testCreate()
```python
python3 main.py create EMP5000 28 "Data Analyst" Finance 3 Onsite 45 Anxiety False
python3 main.py create EMP6000 40 "Data Scientist" IT 15 Hybrid 40 None True
```

Read using testRead()
```python
python3 main.py query
```