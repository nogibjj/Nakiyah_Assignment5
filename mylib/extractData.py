import requests

# Extracting data from Github
def extractData(url="https://raw.githubusercontent.com/viraterletska/Impact_of_Remote_Work_on_Mental_Health/main/data/Impact_of_Remote_Work_on_Mental_Health.csv", 
            file_path="Data/Impact_of_Remote_Work_on_Mental_Health.csv"):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path
        
    else:
        return f"Failed to download file. Status code: {response.status_code}"
