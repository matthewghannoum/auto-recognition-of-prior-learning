import requests

def save_url_as_html(url, filepath):
    response = requests.get(url)
    with open(filepath, "w") as file:
        file.write(response.text)