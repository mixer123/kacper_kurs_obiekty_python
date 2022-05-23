import sqlite3
def connect():
    with sqlite3.connect('baza_modul3.db') as connection:
        ''' Pobrania robimy za pomocą cursora'''
        cursor = connection.cursor()
    return cursor

def getperson(cursor):
    cursor.execute('select * from library ')
    data =[]
    # print(cursor.fetchall())
    for person in cursor.fetchall():
        data.append({
            'email':person[1],
            'name':person[2],
            'tytul':person[3],
            'return':person[4]
        }

        )
    return data

connect= connect()
print(getperson(connect))