import sqlite3
import cgi

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

error = ''
n = ''

def check_user(user):    
    cursor.execute(f"SELECT id FROM users WHERE user = '{user}';")
    existing_user = cursor.fetchone()

    connection.commit()

    return existing_user

def check_email(email):    
    cursor.execute(f"SELECT id FROM users WHERE email = '{email}';")
    existing_email = cursor.fetchone()

    connection.commit()

    return existing_email

def verifyInput(user, email, password):
    global n, result, error
    if ' ' not in user and ' ' not in password and ' ' not in confirmPassword:
        if len(password) >= 4 and len(user) >= 4:
            if password == confirmPassword:
                if validateEmail(email) == True:
                    n = True
                else:
                    error = 'Email is not valid!'
            else:
                error = 'Passwords are not equal!'
        else:
            error = 'User or Password too small!'
    else:
        error = 'Existing spaces!'

def validateEmail(email):
    import re
    patt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    pattern = re.compile(patt)
    return re.match(pattern, email) is not None

result = 'hello'

params = cgi.FieldStorage()

user = params.getfirst('user', '0')
email = params.getfirst('email', '0')
password = params.getfirst('password', '0')
confirmPassword = params.getfirst('confirmPass', '0')

print('Content-type: text/html\n')

verifyInput(user, email, password)

if n == True:
    checkUser = check_user(user)
    checkEmail = check_email(email)
    if checkUser is None:
        if checkEmail is None:
            result = 'true'
            error = 'nothing'
            cursor.execute(f"insert into users (user, email, password) values('{user}', '{email}', '{password}');")
            connection.commit()
        else:
            result = 'false'
            error = 'Email already existing!'
    else:
        result = 'false'
        error = 'User already existing!'
else:
    result = 'false'


connection.close()

print(f'{result}register {error}')