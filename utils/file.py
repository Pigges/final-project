import json

def read(path):
    file = open(path, 'r')
    data = json.loads("".join(file.readlines()))
    file.close()
    return data

def write(path, data):
    file = open(path, 'w')
    file.write(json.dumps(data))
    file.close()