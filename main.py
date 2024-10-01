"""
ETL-Query script
"""

from mylib.loadData import loadData, cleanData
from mylib.queryData import queryData


# Extract
print("Extracting data...")


# Transform and load
print("Transforming data...")
loadData(cleanData())

# Query
print("Querying data...")
print(queryData)