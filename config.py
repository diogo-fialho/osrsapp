import json

SETTINGS_FILES = 'settings.json'

def load_config():
    data = None

    # Open and read the JSON file
    with open(SETTINGS_FILES, 'r') as file:
        data = json.load(file)

    return data
