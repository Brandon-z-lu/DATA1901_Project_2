import requests
import os
from bs4 import BeautifulSoup

# Disable SSL certificate verification
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)
session = requests.Session()
session.verify = False

# Define the URL and fetch the web page
url = "https://en.wikipedia.org/wiki/List_of_Sydney_Trains_railway_stations"
response = session.get(url)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with the list of Sydney Trains railway stations
table = soup.find("table", {"class": "wikitable sortable"})

# Extract the station names from the table
stations = []
for row in table.findAll("tr")[1:]:
    cell = row.findAll("td")[0]
    station_name = cell.get_text(strip=True)
    stations.append(station_name)

# Create the folder 'get_train_station_names_data' if it doesn't exist
os.makedirs('get_train_station_names_data', exist_ok=True)

# Export the station names to a text file
with open('get_train_station_names_data/get_train_station_names_out.txt', 'w') as file:
    for station in stations:
        file.write(f"{station}\n")

print("get_train_station_names done!!")
