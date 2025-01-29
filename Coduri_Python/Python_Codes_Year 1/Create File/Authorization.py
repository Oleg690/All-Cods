def verify(login, password):
    x = open('user.txt', 'r', encoding='utf-8')
    text = x.read()
    x.close()

    users = text.split('\n')
    for i in users:
        user = i.split(';')
        if user[0] == login:
            if user[1] == password:
                return True, ''
            else:
                return False, 'Parola este greșită!'
    return False, 'Login-ul este greșit!'