import sqlite3, cgi

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

error = ''
result = ''

params = cgi.FieldStorage()

verify = params.getfirst('verify', 'login')

user = params.getfirst('user', '0')
password = params.getfirst('password', '0')

print('Content-type: text/html\n')

cursor.execute("select * from users")
x = cursor.fetchall()

def verifyUserOrEmail(toVerify):
    global result, error
    if '@' in toVerify:
        for i in x:
            if user == i[2] and password == i[3]:
                result = 'true'
                error = 'nothing'
                break
            else:
                result = 'false'
                error = 'Email or Password incorect!'
    else:
        for i in x:
            if user == i[1] and password == i[3]:
                result = 'true'
                error = 'nothing'
                break
            else:
                result = 'false'
                error = 'User or Password incorect!'

verifyUserOrEmail(user)

connection.close()

print(f'{result}login {error}')