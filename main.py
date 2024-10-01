"""
ETL-Query script
"""

from mylib.extractData import extractData
from mylib.loadData import loadData, cleanData
from mylib.queryData import queryData


# Extract
print("Extracting data...")
extractData()

# Transform and load
print("Transforming data...")
loadData(cleanData())

# Query
print("Querying data...")
queryData()
