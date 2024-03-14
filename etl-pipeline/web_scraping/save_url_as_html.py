import requests


def get_url_as_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, filepath):
    with open(filepath, "w") as file:
        file.write(html)


def save_url_as_html(url, filepath):
    html = get_url_as_html(url)
    save_html(html, filepath)
