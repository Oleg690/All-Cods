import cgi

print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Tabla inmultirii</title>
</head>
<body>
''')

parametres = cgi.FieldStorage()
x = parametres.getfirst('x', '0')
y = parametres.getfirst('y', '0')

if x == '0' or y == '0':
    print('Nu sunt dati parametri')
else:
    z = int(x) + int(y)
    print(f'{x} + {y} = {z}')

print(
'''
</body>
</html>
''')

#http://127.0.0.1/cgi-bin/index.py?x=3&y=3