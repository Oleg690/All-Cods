import sqlite3

from functions import dbUtils

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

sql = 'drop table groceries'
dbUtils.execSql(sql)

connection.close()