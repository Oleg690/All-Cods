import cgi, sqlite3

connection = sqlite3.connect('C:/Users/crist/OneDrive/Desktop/Cods/Login-Page/Login-Script/sql/database.db')
cursor = connection.cursor()

form = cgi.FieldStorage()

data_input = form.getfirst("dataInput" ,'0')
user = form.getfirst("user" ,'0')

cursor.execute(f"update users set imgUrl = '{data_input}' where user = '{user}'")
connection.commit()

connection.close()