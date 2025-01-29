import sqlite3 #importăm biblioteca sqlite3

connection = sqlite3.connect('data.db')#ne conectăm la baza de date

cursor = connection.cursor() #creăm cursorul, adică executantul nostru pentru a codurile sql

sql = '''CREATE TABLE IF NOT EXISTS groceries(
id integer primary key autoincrement,
name text,
price integer,
comment text
)'''# punem într-o variabilă codul pentru sql pentru a crea tabelul dacă nu există

cursor.execute(sql) #executăm codul înserat în variabilă

cursor.execute("insert into groceries(name, price) values('Tanc', '1000')") #inserăm în tabel niște valori
cursor.execute("insert into groceries(name, price) values('Avion de lupta', '2000')")#inserăm în tabel niște valori
cursor.execute("insert into groceries(name, price) values('Rosii', '3')") #inserăm în tabel niște valori

connection.commit() #salvăm toate codurile care sau executat

cursor.execute('select * from groceries') #selectăm tot din tabel
x = cursor.fetchall()# inserăm tot din tabel in variabila x

print(x) #arătăm valorile

connection.close() #închidem  conecțiunea cu baza de date