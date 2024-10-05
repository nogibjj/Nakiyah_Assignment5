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
├── main.py
├── test.py
├── Makefile
├── mylib/
│   ├── extractData.py
│   ├── loadData.py
│   └── queryData.py
├── README.md
├── Requirements.txt
├── database1.db
├── testOutputs.md
└── query_log.md

```
## Purpose of this project

Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline that processes data from external public datasets and stores it in a SQLite database. The key stages of the pipeline are as follows:

Extract:

Data is fetched from a public GitHub repository and loaded into a local CSV file.
Transform:

The CSV file is cleaned and pre-processed, ensuring the data is structured correctly and ready for analysis. This may include handling missing values, normalizing data types, and filtering out invalid entries.
Load:

The cleaned data is then loaded into a SQLite .db file, where it can be efficiently queried for further analysis.
Query:

SQL queries are run against the database to retrieve insights or verify data integrity.
Unit Testing
To ensure the robustness of the ETL process, a suite of unit tests is included. These tests are executed using Python's subprocess module to simulate the full pipeline, testing each stage for correctness. The tests validate the following:

Extraction: Ensures that the data is correctly fetched and saved as a CSV file.
Transformation: Verifies that the cleaning and transformation steps produce the expected results.
Loading: Confirms that the data is properly inserted into the SQLite database.
SQL Queries: Checks the results of SQL queries for accuracy and consistency.