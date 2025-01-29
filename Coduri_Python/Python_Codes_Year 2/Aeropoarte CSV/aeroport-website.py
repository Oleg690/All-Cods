import sqlite3
import webbrowser

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

while True:
    city = input('Introduceți numele orașului: ')

    if city == '':
        break

    city = "'" + city + "'"

    cursor.execute(f"SELECT * FROM airports WHERE city_eng = {city}")
    x = cursor.fetchall()

    if len(x) == 0:
        print(f'Aeroport în orașul {city} nu a fost găsit!')
    elif len(x) == 1:
        web_site = x[0][-1]

        if web_site == None:
            print(f'Web Site pentru aerp din orașul {city} nu există!')
        else:
            webbrowser.open(web_site)
    elif len(x) > 1:
        y = 0
        print('Sau găsit mai multe aeropoarte în acel oraș.')

        for i in x:
            y += 1
            print(f'{y}. Aeroport Name: {i[1]}, City: {i[3]}, WebSite: {i[8]}')

        aerp = input('Introduceți numele aeroportului care doriți: ')

        if aerp.isdigit():
            aerp = int(aerp)
            aerp -= 1
        else:
            print('Introduceți un numar!')
            continue

        web_site = x[aerp][-1]

        if web_site == None:
            print(f'Web Site pentru aeroportului din orașul {city} nu există!')
        else:
            webbrowser.open(web_site)
    else:
        print('Nu sa găsit nici un oraș!')

connection.close()