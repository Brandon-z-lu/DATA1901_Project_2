import os


def get_suburbs_by_areas(area_name, file_path):
    """
    Returns a list of suburbs in the input area.
    :param area_name: str, name of the area to search suburbs in
    :param file_path: str, path to the file containing suburbs
    :return: list of str, suburbs in the input area
    """
    area_suburbs = []
    area_found = False
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == area_name:
                area_found = True
            elif area_found and line.strip() == '':
                break
            elif area_found:
                area_suburbs.append(line.strip())
    return area_suburbs


def export_suburbs_by_areas(file_path):
    """
    Exports suburbs by areas into separate files in a given directory.
    :param file_path: str, path to the file containing suburbs
    """
    directory = "get_suburbs_by_areas_data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'r') as file:
        suburbs = file.read().splitlines()
    areas = set(suburbs)  # set of unique area names
    for area_name in areas:
        area_suburbs = get_suburbs_by_areas(area_name, file_path)
        area_file_path = os.path.join(directory, f"{area_name}.txt")
        directory_parts = area_file_path.split(os.path.sep)[:-1]
        current_path = ''
        for part in directory_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        with open(area_file_path, 'w') as file:
            file.write('\n'.join(area_suburbs))


file_path = "get_suburbs_by_areas_data/All_Stake_Supply.txt"
export_suburbs_by_areas(file_path)
