import requests
from bs4 import BeautifulSoup

url = 'https://www.quotegarden.com/mind.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all('font', class_='quote')

for quote in quotes:
    text = quote.get_text(strip=True)
    print(text)
