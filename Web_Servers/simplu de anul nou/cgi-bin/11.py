import cgi
import sqlite3
import random

print('''
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
''')

key = ''
database_path = 'cgi-bin/database.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

sql =   'create table if not exists users(' \
        'id integer primary key autoincrement,' \
        'cadouri text)'

cursor.execute(sql)

params = cgi.FieldStorage()
x = params.getfirst('x', '0')

temporaryData = []
if x != '0':
    cursor.execute('SELECT * FROM users;')
    o = cursor.fetchall()
    for i in o:
        temporaryData.append(i[1])
    if x not in temporaryData:
        cursor.execute(f'insert into users (cadouri) values("{x}")')
        connection.commit()

cursor.execute('SELECT * FROM users')
n = cursor.fetchall()
connection.commit()
random_gift = random.randint(0, len(n)-1)
result = ''
k = 1
for i in n:
    if k == len(n):
        result += str(i[1])
    else:
        result += str(i[1]) + ', '
    k += 1

print("<p>" + n[random_gift][1] + "</p>")
print("<button id='1'>Randomise</button>")

print("<p id='4'></p>")
print("<button id='2' onclick=''>See full list</button>")

print('''<script>''')
print('''
let randomBtn = document.getElementById('1');
let seeList = document.getElementById('2');
let deleteList = document.getElementById('3');
let resultParagraf = document.getElementById('4');

function reloadPage() {
    location.reload();
}

randomBtn.addEventListener('click', reloadPage)

function showResult(){''')
print(f'''resultParagraf.innerHTML = "<p id='4'> {result} </p>"''')
print('''}

seeList.addEventListener('click', showResult)''')

print('''
    </script>
</body>
</html>
''')
connection.close()