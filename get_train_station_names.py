import requests
from bs4 import BeautifulSoup
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
warnings.simplefilter('ignore', InsecureRequestWarning)


URL = 'https://nswtrains.fandom.com/wiki/list_of_stations_by_local_government_area'

# Disable SSL verification
session = requests.Session()
session.verify = False

# Use the session to send a GET request to the URL
page = session.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='mw-content-text')
rows = results.find_all('tr')

for row in rows:
    data = row.find_all('td')
    if len(data) == 3:
        print(data[0].text.strip())

print("Done!")
