import sys
from mylib.extractData import extractData
from mylib.loadData import loadData, cleanData
from mylib.queryData import createOrUpdateRecord


# Extract
print("Extracting data...")
extractData()

# Transform and load
print("Transforming data...")
loadData(cleanData())

# Query
print("Querying data...")

operation = sys.argv[1]
if operation == "create":
    id = sys.argv[2]
    age = sys.argv[3]
    jobrole = sys.argv[4]
    industry = sys.argv[5]
    experience = sys.argv[6]
    worklocation = sys.argv[7]
    hoursworked = sys.argv[8]
    mhcondition = sys.argv[9]
    access = sys.argv[10]
    print("Create Record")
    createOrUpdateRecord(id, age, jobrole, industry, experience,
                         worklocation, hoursworked, mhcondition, access)
