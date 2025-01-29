import sqlite3, json, cgi

params = cgi.FieldStorage()

goods = params.getfirst('goods', '0')
goods = json.loads(goods)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

expresion = ''

for i in goods:
    expresion += i + ','

expresion += '-1'

cursor.execute(f'SELECT * FROM groceries where id in ({expresion});')
x = cursor.fetchall()

print(str(x[0][0]))

connection.close()

html = "<table width='300px' align='center'>"
html += "<tr> <td colspan='4'> Items in the Cart</td> </tr>"
html += "<tr><td>Id</td> <td>Product</td> <td>Price</td> <td>Comment</td></tr>"

for i in x:
    html += '<tr>'

    for j in i:
        html += '<td>' + str(j) + '</td>'
    
    html += '</tr>'

html += '</table>'

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../style.css">
    <title>Cart</title>
</head>
<body>
''' + html + '''
</body>
</html>
''')