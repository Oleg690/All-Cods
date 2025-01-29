import sqlite3

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

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

def verifyInput(user, email, password, confirmPassword):
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
    
    return n

def validateEmail(email):
    import re
    patt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    pattern = re.compile(patt)
    return re.match(pattern, email) is not None

connection.close()