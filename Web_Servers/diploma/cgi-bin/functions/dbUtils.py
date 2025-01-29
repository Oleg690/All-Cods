import sqlite3, json

def execSql(sql):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    print('Content-type: text/html\n')

    cursor.execute(sql)
    connection.commit()

    showTable(cursor)
    connection.close()
    

def showTable(cursor):
    cursor.execute('select * from groceries;')
    x = cursor.fetchall()

    result = "<tr><td>Id</td> <td>Product</td> <td>Price</td> <td>Comment</td> <td>Check</td></tr>"

    for i in x:
        result += '<tr>'

        for j in i:
            result += '<td>' + str(j) + '</td>'
        
        result += "<td><input type='checkbox' class='checkBox' id='" + str(i[0]) + "'onchange='check_box_click(this)' ></td>"

        result += '</tr>'
    
    result = json.dumps(result)

    print(result)