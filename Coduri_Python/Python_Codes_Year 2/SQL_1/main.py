# Tabele
# Campuri -> inregistrari
# Camp -> Coloana
# Inregistrari -> linie

import sqlite3

database_path = 'Python Codes Year 2\SQL_1\database.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

sql =   'create table if not exists users(' \
        'number1 text,'\
        'multiply text,'\
        'number2 text,'\
        'equal text,'\
        'number3 text)'

cursor.execute(sql)

# cursor.execute('insert into users values("admin", "123")')
# cursor.execute('insert into users values("user", "111")')
y = 0
o = 0

for i in range(0,10):
        y += 1
        o += 3
        cursor.execute(f'insert into users values("3", "x", "{y}", "=", "{o}")')

connection.commit()

connection.close()

print('Successfully loaded!')

# create table:
# text - va contine date de tip text
# integer - va contine numere

# insert:
# insert into (tabelul nostru) values(data1, data2)
# insert into (tabelul nostru) values(text, integer)

# select:
# select * from (Table Name)
# * -> toate datele din tabel
# .fetchall()
# Cum se afișează -> [('admin', '123'), ('user', '111')]


#!!!!!!!!!!!!!!!!!!!!!!!!
#DROP TABLE (table_name); --> in SQL3 app