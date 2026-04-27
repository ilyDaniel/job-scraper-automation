import requests
from bs4 import BeautifulSoup

URL = "https://example.com/careers"

response = requests.get(URL)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)
print("Fetched page")
print(len(response.text))