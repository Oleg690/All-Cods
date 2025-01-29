import cgi, sqlite3, json

print('Content-type: text/html\n')

connection = sqlite3.connect('C:/Users/crist/OneDrive/Desktop/Cods/Login-Page/Login-Script/sql/database.db')
cursor = connection.cursor()

form = cgi.FieldStorage()

info = form.getfirst('user', '0')

if '@' in info:
    cursor.execute(f"select imgUrl from users where email = '{info}';")
    data = cursor.fetchall()
else:
    cursor.execute(f"select imgUrl from users where user = '{info}';")
    data = cursor.fetchall()

print(json.dumps(data[0][0]))

connection.close()