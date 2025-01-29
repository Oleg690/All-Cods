import sqlite3, json

def sendReq(sql):
    connection = sqlite3.connect('sql/database.db')
    cursor = connection.cursor()

    cursor.execute(sql)
    x = cursor.fetchall()

    connection.close()

    result = json.dumps(x)

    return result