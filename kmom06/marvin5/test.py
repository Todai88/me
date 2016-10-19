"""
TEST"""

import requests
from bs4 import BeautifulSoup

#Setting up variables
req = requests.get("https://google.com")
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
