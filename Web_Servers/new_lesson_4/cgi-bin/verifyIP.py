import cgi

params = cgi.FieldStorage()

x = params.getfirst('x', 0)

print('Content-type: text/html\n')

result = ''
y = str(x).split('.')

if len(y) == 4:
    for i in y:
        if int(i) < 256 and int(i) >= 1:
            result = 'Corect'
        else:
            result = 'Gresit'
            break
else:
    result = 'Gresit'

print(result)