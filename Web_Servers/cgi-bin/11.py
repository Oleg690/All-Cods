import cgi
import sqlite3
import random

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
''')

database_path = 'cgi-bin/database.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

sql =   'create table if not exists users(' \
        'cadouri text)'

cursor.execute(sql)

params = cgi.FieldStorage()
x = params.getfirst('x', '0')

cursor.execute(f'insert into users values("{x}")')
connection.commit()

cursor.execute('SELECT * FROM users')
n = cursor.fetchall()
connection.commit()

random_gift = random.randint(0, len(n)-1)

print("<p>" + n[random_gift][0] + "</p>")

connection.close()

print('''
</body>
</html>
''')