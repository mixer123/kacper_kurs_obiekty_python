import sqlite3
def connect():
    with sqlite3.connect('baza.db') as connection:
        ''' Pobrania robimy za pomocą cursora'''
        cursor = connection.cursor()
    return cursor

def getauthors(cursor):
    cursor.execute('select * from books where author=?', ('sienkiewicz',))
    data =[]
    for book in cursor.fetchall():
        data.append({
            'title':book[1],
            'author':book[2]
        }

        )
    return data


connect= connect()
print(getauthors(connect))