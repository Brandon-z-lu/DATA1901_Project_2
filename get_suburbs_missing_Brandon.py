import os

'''
:param: "main1_INPUT.txt" as the input
:return: compare the "main1_INPUT.txt" with the "csv_cache/" file names, 
if not included, run the "python3 get_suburbs.py" to 
write to "get_suburbs_data/get_suburbs_out.txt"
'''


def extract_suburb_name(line):
    return line.split("/")[-2].strip()


def write_suburbs_to_file(suburb_names):

    # check if directory exists, and create it if it doesn't
    if not os.path.exists("Get_Suburbs_missing_Brandon"):
        os.makedirs("Get_Suburbs_missing_Brandon")
    with open("Get_Suburbs_missing_Brandon/Suburbs_missing.txt", "w") as f:
        for suburb_name in suburb_names:
            f.write(f"{suburb_name}\n")
    print("Get_Suburbs_missing_Brandon/Suburbs_missing.txt DONE!")


def main():
    with open("main1_INPUT.txt", "r") as f:
        suburbs_content = f.readlines()
    suburb_names = [extract_suburb_name(line) for line in suburbs_content]
    csv_files = os.listdir("csv_cache")
    missing_suburbs = []
    for suburb_name in suburb_names:
        found = False
        for csv_file in csv_files:
            if suburb_name in csv_file:
                found = True
                break
        if not found:
            missing_suburbs.append(suburb_name)
    if missing_suburbs:
        write_suburbs_to_file(missing_suburbs)
    else:
        print("All suburbs found in csv_cache")


if __name__ == "__main__":
    main()
