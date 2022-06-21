import yaml

'''Czytam yaml-a'''
with open('conf2.yaml', 'r') as file:
    data_yaml = yaml.safe_load_all(file)
    # print(data_yaml)
    print(next(data_yaml)) # II sposób iterartor
    for line in data_yaml: # I sposób
        print(line)

'''data_yaml jest generatorem. Można go przeczytać w następujący sposób - jak wyżej'''

