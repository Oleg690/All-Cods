import sqlite3

database_path = 'Python Codes Year 2\database_example\database.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

sql =   'create table if not exists users(' \
        'text text)'

cursor.execute(sql)

cursor.execute('insert into users values("Hello")')

connection.commit()

connection.close()

print('Successfully loaded!')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#DROP TABLE (table_name); --> in SQL3