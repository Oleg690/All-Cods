import sqlite3
import cgi

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

params = cgi.FieldStorage()

user = params.getfirst('user', '0')
email = params.getfirst('email', '0')

print('Content-type: text/html\n')

cursor.execute(f"delete from users where user = '{user}' and email = '{email}';")
connection.commit()

connection.close()