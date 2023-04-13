import requests
import sys
import os
import json
import re

# HOW TO USE IT!!!!!!!!! =====================================================================================
# python get_suburbs.py
# ============================================================================================================

# Function to find the latitude and longitude of a train station in the given suburb

# Replace YOUR_API_KEY with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = "AIzaSyDK-O4xQuZ5L1bytY43idAANedr7Ix5ld0"


def find_suburb(suburb):
    search_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={suburb}+train+station+Sydney+NSW&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(search_url)
    result = json.loads(response.text)

    if "results" not in result or len(result["results"]) == 0:
        print(
            f"Error processing suburb '{suburb}': Could not find train station information")
        return None, None, None

    lat = result["results"][0]["geometry"]["location"]["lat"]
    lng = result["results"][0]["geometry"]["location"]["lng"]
    formatted_address = result["results"][0]["formatted_address"]

    # Extract the postcode from the formatted address
    postcode = None
    match = re.search(r"\b\d{4}\b", formatted_address)
    if match:
        postcode = match.group()

    return postcode, lat, lng


def main(input_file, output_file):
    with open(input_file, "r") as f_in:
        suburbs = [line.strip() for line in f_in.readlines()
                   if not line.strip().startswith("#")]

    num_suburbs = len(suburbs)
    print(f"Begin: 0/{num_suburbs}")

    not_found = []

    with open(output_file, "w") as f_out:
        for index, suburb in enumerate(suburbs):
            postcode, lat, lng = find_suburb(suburb)
            if postcode and lat and lng:
                f_out.write(f'{postcode}/{suburb}/, {lat}, {lng}\n')
                print(f"{index + 1}/{num_suburbs}: {suburb} {postcode}")
            else:
                print(f"{index + 1}/{num_suburbs}: {suburb} NOT FOUND!!!")
                not_found.append(suburb)


if __name__ == "__main__":
    folder_name = "get_suburbs_data"
    os.makedirs(folder_name, exist_ok=True)

    input_file_name = os.path.join(folder_name, "get_suburbs_in.txt")
    output_file_name = os.path.join(folder_name, "get_suburbs_out.txt")

    main(input_file_name, output_file_name)
