"""
Simple utility functions for working with json files
"""

import json

def read(path):
    """
    Method to easily retrieve the data in a file in json format

    Keyword arguments:
    path -- path to the file to read
    """
    data = {}
    try:
        with open(path, "r", encoding='utf-8') as file:
            data = json.loads("".join(file.readlines()))
    except NameError:
        print(f"{path} does not exist. Creating...")
        write(path, data)
    return data

def write(path, data):
    """
    Method to easily write the data to a file in json format

    Keyword arguments:
    path -- path to the file to write
    data -- data to write to the file
    """
    with open(path, "w", encoding='utf-8') as file:
        file.write(json.dumps(data))
