import smtplib, cgi, random, sqlite3
from password import passwordAccount

code = ''
verification = False

connection = sqlite3.connect('sql/database.db')
cursor = connection.cursor()

cursor.execute('select email from users')
emails = cursor.fetchall()

params = cgi.FieldStorage()

email = params.getfirst('email', '0')

for i in emails:
    if email == i[0]:
        verification = True
        break
    else:
        verification = False

for i in range(6):
    code += str(random.randint(0,9))


host = 'smtp-mail.outlook.com'
port = 587

from_email = 'passwordresetoriginal542@outlook.com'
to_email = email
password = passwordAccount

message = f"Subject: Your code is: {code}"

print('Content-type: text/html\n')

def sendEmail():
    global status_code, responce, e
    try:
        smtp = smtplib.SMTP(host, port)
        status_code, responce = smtp.ehlo()
        status_code, responce = smtp.starttls()
        status_code, responce = smtp.login(from_email, password)
        smtp.sendmail(from_email, to_email, message)
        smtp.quit()
        print(str(code))
    except Exception as e:
        print(f'Email is not registrated!')

if verification == True:
    sendEmail()
else:
    print('Email is not registrated!')