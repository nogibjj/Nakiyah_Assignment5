import sys
from mylib.extractData import extractData
from mylib.loadData import loadData, cleanData
from mylib.queryData import queryData, createOrUpdateRecord, deleteRecord


def main():
    if len(sys.argv) < 2:
        print("Please specify an operation: extract, load, query, create, delete.")
    else:
        operation = sys.argv[1]
        if sys.argv[1] == "extract":
            print("Extracting data...")
            extractData()

        elif sys.argv[1] == "load":
            print("Transforming data...")
            data = cleanData()
            loadData(data)

        elif operation == "query":
            print("Querying data...")
            queryData()

        elif operation == "create":
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
            createOrUpdateRecord(
                id,
                age,
                jobrole,
                industry,
                experience,
                worklocation,
                hoursworked,
                mhcondition,
                access,
            )

if __name__ == "__main__":
    main()