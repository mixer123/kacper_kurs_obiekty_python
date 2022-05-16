import sqlite3
from sqlite import getauthors
def test_getauthors():
     conn = sqlite3.connect(':memory:')
     cursor = conn.cursor()
     cursor.execute('''
     create table books (id integer, title text, author text , created text)
     ''')
     sample_data = [(1,'potop', 'sienkiewicz', '2022-12-01'),
                    (2,'LOKOMOTYWA', 'sienkiewicz','2022-01-12')]
     cursor.executemany('INSERT INTO books VALUES (?,?,?,?)', sample_data)

     data = getauthors(cursor)
     print(data)
     assert data[0]=={'title':'potop', 'author':'sienkiewicz'}

