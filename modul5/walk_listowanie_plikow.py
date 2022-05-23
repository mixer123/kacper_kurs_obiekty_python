''' Listujemy katalog a pozniej tworzymy podobną strukturę'''
import os
from os import walk, makedirs, rmdir
from shutil import rmtree

target = 'result'
rmtree(target)
for path, dirs, files in walk('cos'):
    makedirs(f'{target}/{path}', exist_ok=True)
    print(path)
    for file in files:
        print(file)
        open(f'{target}/{path}/{file}','a').close()