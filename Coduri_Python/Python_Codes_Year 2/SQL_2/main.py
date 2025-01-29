import sqlite3

database_path = 'Python Codes Year 2\SQL_2\database.db'
connection = sqlite3.connect(database_path)

cursor = connection.cursor()

sql = "create table if not exists phonenumbers(" \
      "Name text," \
      "Phone integer" \
      ");"

cursor.execute(sql)

while True:
      o = 'Nimic'
      x = int(input("Alegeți operația (1 - insert, 2 - select, 3 - exit): "))
      
      if x == 1:
            y = input('Introduceți numele numarului de telefon: ')
            z = input('Introduceți numarul de telefon: ')

            if y != '' and z != '':
                  if 7 <= len(z) <= 15:
                        cursor.execute(f'insert into phonenumbers values("{y}", "{z}")')
                        connection.commit()
                        print('Abonatul a fost adăugat cu succes!')
                  else:
                        print('Numarul de telefon are mai multe sau mai puține numere de cât trebuie!')
            else:
                  print('Trebuie să completați toate spațiile')
      elif x == 2:
            j = 1
            cursor.execute('select * from phonenumbers')
            numbers = cursor.fetchall()
            for i in numbers:
                  print(f"{j}.Nume: {i[0]}; Telefon: {i[1]};")
                  j += 1
      elif x == 3:
            connection.close()
            break
      else:
            print('Numarul introdus nu este corect!')

print('By, by!')
print()