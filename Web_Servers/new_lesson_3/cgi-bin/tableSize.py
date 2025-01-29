import cgi

params = cgi.FieldStorage()

x = int(params.getfirst('x', 0))

print('Content-type: text/html\n')

result = ''

k = 2

for i in range(x):
    result += '<tr height="100px">'
    for i in range(x):
        j = k % 2
        if j == 0:
            n = i % 2
            if n == 0:
                result += '<td width="100px" bgcolor="black">'
            else:
                result += '<td width="100px" bgcolor="white">'
        else:
            n = i % 2
            if n != 0:
                result += '<td width="100px" bgcolor="black">'
            else:
                result += '<td width="100px" bgcolor="white">'
    result += '</tr>'
    k += 1
print(result)