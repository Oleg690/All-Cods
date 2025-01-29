import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute("select count(country_rus) from airports group by country_rus")
x = cursor.fetchall()

o = []

for i in x:
    o.append(i)

o.sort(reverse=1)

print(f"Cele mai multe aeropoarte sunt: 1.{o[0][0]}, 2.{o[1][0]}, 3.{o[2][0]} ")

connection.close()