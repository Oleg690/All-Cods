import cgi, sqlite3

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

error = 'Nothing'
result = 'False'

params = cgi.FieldStorage()

verify = params.getfirst('verify', 'login')
email = params.getfirst('email', '0')
password = params.getfirst('password', '0')
confirmPassword = params.getfirst('confirmPsw', '1')

print('Content-type: text/html\n')

def passwordValide(password, confirmPassword):
    global x, result, error

    cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    x = cursor.fetchall()

    if ' ' not in password and ' ' not in confirmPassword:
        if len(password) >= 4:
            if password == confirmPassword:
                if x[0][3] != str(password):
                    cursor.execute(f"update users set password = '{password}' where email = '{email}';")
                    connection.commit()
                    result = 'True'
                    error = 'Nothing'
                else:
                    error = 'Existing password!'
                    result = 'False'
            else:
                error = 'Passwords are not equal!'
                result = 'False'
        else:
            error = 'Password too small!'
            result = 'False'
    else:
        error = 'Existing spaces!'
        result = 'False'
    

passwordValide(password, confirmPassword)

print(f'{result} {error}')

connection.close()