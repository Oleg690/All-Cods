import sqlite3

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

def createTable():
    sql = '''CREATE TABLE IF NOT EXISTS users(
    id integer primary key autoincrement,
    user text,
    email text,
    password text,
    imgUrl text
    )'''
    cursor.execute(sql)
    connection.commit()

createTable()

connection.close()