import cgi

print('''
<!DOCTYPE html>
<html>
<head>
    <title>Tabla inmultirii</title>
</head>
<body>
''')

parametres = cgi.FieldStorage()
x = parametres.getfirst('x', '0')

print(
'''
</body>
</html>
''')