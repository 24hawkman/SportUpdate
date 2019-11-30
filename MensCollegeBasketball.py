import sys
import requests
from bs4 import BeautifulSoup
import SMS


response_text = requests.get('https://www.espn.com/mens-college-basketball/scoreboard').text
soup = BeautifulSoup(response_text, 'html.parser')
html_text = soup.get_text()

print(html_text)

