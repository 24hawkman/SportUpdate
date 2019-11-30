import sys
import requests
from bs4 import BeautifulSoup
import SMS


response_text = requests.get('https://www.cbssports.com/college-basketball/scoreboard/').text
soup = BeautifulSoup(response_text, 'html.parser')
html_text = soup.get_text()

start = html_text.find('1\n2\nT\n')
html_text = html_text[start:len(html_text)]

file = open('html_data.txt', 'w')
file.write(html_text)
file.close()

print(html_text)

