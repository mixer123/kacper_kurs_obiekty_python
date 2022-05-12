import json
with open('test.json') as file:
    data = json.load(file)
    print(type(data))

    for item in data.items():
        print(item)