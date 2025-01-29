import cgi, sqlite3, json

print('Content-type: text/html\n')

connection = sqlite3.connect('C:/Users/crist/OneDrive/Desktop/Cods/Login-Page/Login-Script/sql/database.db')
cursor = connection.cursor()

params = cgi.FieldStorage()

user = params.getfirst('user', '0')
email = params.getfirst('email', '0')
password = params.getfirst('password', '0')

userCurrent = params.getfirst('userCurrent', '0')
emailCurrent = params.getfirst('emailCurrent', '0')

error = ''

def verify(user, email, password):
    global error, userCurrent, emailCurrent
    result = False
    if user != '0' and email != '0' and password != '0':
        if check_user(user) == None:
            if check_email(email) == None:
                if verifyInput(user, email, password) == True:
                    cursor.execute(f"select id from users where user = '{userCurrent}' and email = '{emailCurrent}'")
                    id_ = cursor.fetchall()
                    result = True
            else:
                error = ['Email already taken!']
        else:
            error = ['User already taken!']
    else:
        error = ['Fill all the inputs!']

    if result == True:
        return [result, id_]
    else:
        return [result, error]

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
    global error
    verify = False
    if ' ' not in user and ' ' not in password:
        if len(password) >= 4 and len(user) >= 4:
            if validateEmail(email) == True:
                verify = True
            else:
                error = ['Email is not valid!']
        else:
            error = ['User or Password too small!']
    else:
        error = ['Existing spaces!']

    return verify

def validateEmail(email):
    import re
    patt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    pattern = re.compile(patt)
    return re.match(pattern, email) is not None

info = verify(user, email, password)

if info[0] == True:
    cursor.execute(f"update users set user = '{user}', email = '{email}', password = '{password}' where id = {info[1][0][0]};")
    connection.commit()
    infoToSend = user, email
    print(json.dumps(infoToSend))
else:
    print(json.dumps(info[1]))

connection.close()