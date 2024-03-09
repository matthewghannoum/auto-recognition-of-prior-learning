import requests

def saveUrlAsHTML(url, filepath):
    response = requests.get(url)
    with open(filepath, "w") as file:
        file.write(response.text)