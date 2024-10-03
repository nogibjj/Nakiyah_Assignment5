import sys
from mylib.extractData import extractData
from mylib.loadData import loadData, cleanData
from mylib.queryData import queryData, createOrUpdateRecord, querySpecificRecord, deleteRecord

def main():
    if sys.argv[1] == "extract":
        print("Extracting data...")
        extractData()

    elif sys.argv[1] == "load":
        print("Transforming data...")
        data = cleanData()
        loadData(data)

    elif sys.argv[1] == "query":
        print("Querying data...")
        queryData(20)

    elif sys.argv[1] == "create":
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
        
    elif sys.argv[1] == "query_specific":
        print("Querying specific record...")
        id = sys.argv[2]
        querySpecificRecord(id)

    elif sys.argv[1] == "delete":
        print("Deleting selected query...")
        id = sys.argv[2]
        deleteRecord(id)

if __name__ == "__main__":
    main()
