import cgi, sqlite3, json

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

params = cgi.FieldStorage()

info = params.getfirst('info', '0')
verify = params.getfirst('verify', '0')

def selectPy(info):
    cursor.execute('select price from groceries')
    x = cursor.fetchall()

    if info == 'avg':
        result = 'Average Price: '
        counter = 0
        for i in x:
            counter += i[0]
        toSend = counter / len(x)
    elif info == 'min':
        result = 'Minimum Price: '
        toSend = float('inf')
        for i in x:
            if i[0] < toSend:
                toSend = i[0]
    elif info == 'max':
        result = 'Maximum Price: '
        toSend = float('-inf')
        for i in x:
            if i[0] > toSend:
                toSend = i[0]

    result += str(toSend)
    result = json.dumps(result)

    print(result)


def selectSQL(intepretor):
    cursor.execute(f"select {intepretor}(price) from groceries;")
    x = cursor.fetchall()

    if intepretor == 'min':
        result = 'Minimum Price: '
    elif intepretor == 'max':
        result = 'Maximum Price: '
    elif intepretor == 'avg':
        result = 'Average Price: '

    result += str(x[0][0])
    result = json.dumps(result)

    print(result)

if verify == 'sql':
    selectSQL(info)
if verify == 'py':
    selectPy(info)

connection.close()