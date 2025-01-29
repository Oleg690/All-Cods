import sqlite3
from functions import dbUtils

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

dbUtils.showTable(cursor)

connection.close()