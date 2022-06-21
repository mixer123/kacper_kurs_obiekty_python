import json
import yaml
"""Czytamy jsona"""
with open('conf.json', 'r') as file:
    data_json = json.load(file)
    print(data_json)
'''Czytam yaml-a'''
with open('conf.yaml', 'r') as file:
    data_yaml = yaml.safe_load(file)
    print(data_yaml)