import sqlite3, cgi, json, random

print('Content-type: text/html\n')

connection = sqlite3.connect('C:/Users/crist/OneDrive/Desktop/Cods/Login-Page/Login-Script/sql/database.db')
cursor = connection.cursor()

params = cgi.FieldStorage()

user = params.getfirst('user', 'user')
email = params.getfirst('email', 'example@gmail.com')

cursor.execute(f"select password from users where user = '{user}' and email = '{email}'")
resultPassword = cursor.fetchone()

def getRandomValue(length):
    result = ''
    alphabetBig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lists = [alphabetBig, alphabetSmall, numbers]

    for i in range(length):
        x = random.choice(lists)
        result += random.choice(x)
    
    return result

valueToSend = getRandomValue(len(resultPassword[0]))

valueToSend = json.dumps(valueToSend)

print(valueToSend)

connection.close()