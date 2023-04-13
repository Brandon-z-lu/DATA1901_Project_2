import os

# Function to extract suburb names from a line in suburbs.txt
def extract_suburb_name(line):
    return line.split("/")[-2].strip()

# Read the contents of suburbs.txt
with open("suburbs.txt", "r") as f:
    suburbs_content = f.readlines()

# Extract suburb names
suburb_names = [extract_suburb_name(line) for line in suburbs_content]

# List all files in csv_cache folder
csv_files = os.listdir("csv_cache")

# Loop through suburb names and check if any file contains the suburb name
for suburb_name in suburb_names:
    found = False
    for csv_file in csv_files:
        if suburb_name in csv_file:
            found = True
            break

    if not found:
        print(f"{suburb_name}")
