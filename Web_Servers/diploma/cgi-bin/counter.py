import sqlite3

print('Content-type: text/html \n')

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('SELECT count(*) FROM groceries;')
x = cursor.fetchall()

print(str(x[0][0]))

connection.close()