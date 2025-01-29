import cgi

params = cgi.FieldStorage()

x = int(params.getfirst('x', 0))
y = int(params.getfirst('y', 0))

operation = params.getfirst('operation', 0)

print('Content-type: text/html\n')

if operation == 'plus':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '×':
    print(x * y)
elif operation == '÷':
    print(x / y)