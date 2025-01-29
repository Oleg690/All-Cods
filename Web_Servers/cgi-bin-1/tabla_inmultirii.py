print('''
<!DOCTYPE html>
<html>
<head>
    <title>Tabla inmultirii</title>
</head>
<body>
    <p><b>Tabla inmultirii cu trei:</b></p>
''')

tabla = []
o = 0
r = 0

for i in range(0, 10):
    r += 1
    o = 0
    print('<br>')
    for k in range(0, 10):
        o += 1
        suma = r * o
        x = f'{r} x {o} = {suma}'
        print('<p>' + x + '</p>')

print(
'''
</body>
</html>
''')