import json

def read(path):
    data = {}
    try:
        file = open(path, 'r')
        data = json.loads("".join(file.readlines()))
        file.close()
    except:
        print(f"{path} does not exist. Creating...")
        file = open(path, 'w')
        file.write(json.dumps(data))
        file.close()
    return data

def write(path, data):
    file = open(path, 'w')
    file.write(json.dumps(data))
    file.close()