import requests
import sys
import os
import json

# HOW TO USE IT!!!!!!!!! =====================================================================================
# python get_suburbs_list.py suburbs_of_interests.txt suburbs_scrapped.txt
# ============================================================================================================

# Function to find the latitude and longitude of a train station in the given suburb

# Replace YOUR_API_KEY with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = "AIzaSyDK-O4xQuZ5L1bytY43idAANedr7Ix5ld0"


def find_suburb(suburb):
    search_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={suburb}+train+station+Sydney+NSW&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(search_url)
    result = json.loads(response.text)

    # Add the following line to print the API response
    print(f"API response for suburb '{suburb}': {result}")

    if "results" not in result or len(result["results"]) == 0:
        print(
            f"Error processing suburb '{suburb}': Could not find train station information")
        return None, None

    lat = result["results"][0]["geometry"]["location"]["lat"]
    lng = result["results"][0]["geometry"]["location"]["lng"]

    return lat, lng





def main(input_file, output_file):
    if not os.path.exists(input_file):
        print("Input file doesn't exist")
        return

    with open(input_file, "r") as f:
        suburbs = [line.strip()
                   for line in f if not line.startswith("#") and line.strip()]

    with open(output_file, "w") as f:
        for suburb in suburbs:
            lat, lng = find_suburb(suburb)
            if lat is not None and lng is not None:
                f.write(f'"{suburb}/", {lat}, {lng}\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_suburbs_list.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
