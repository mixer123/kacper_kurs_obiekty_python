import json
with open('action.json') as file:
    data = json.load(file)
    print(type(data))

    # for item in data.items():
    #     print(item)
    #     print(item[1][0]['click button mouse'])

    # print(data.keys())
# print(data)
def my_func(click,type):
    print(click)
    print(type)
    # print(c)
# my_func(*data) # wypakowanie kluczy slownika
my_func(**data) # wypakowanie wartosci slownika