import sqlite3

connection = sqlite3.connect('diary.db')

cursor = connection.cursor()

create = '''create table if not exists proggress(
         id integer primary key autoincrement,
         subject text,
         grade integer);
'''

cursor.execute(create)
connection.commit()

subjects = [
    ['informatica', 'Informatica'],
    ['biologia', 'Biologia'],
    ['engleza', 'Limba Engleză'],
    ['matematica','Matematica'],
    ['chimia', 'Chimia'],
    ['romana', 'Limba Română'],
    ['fizica', 'Fizica'],
    ['istoria', 'Istoria'],
    ['rusa', 'Limba Rusă'],
    ['tehnologica', 'Educația Tehnologică'],
    ['geografia', 'Geografia'],
    ['muzica', 'Educația Muzicală'],
    ['sănătatea', 'Educația pentru Sănătate']]

def verify():
    global verifyShow

    if check[1] == 'avg' or check[1] == 'group':
        verifyShow = True
    else:
        verifyShow = False
def add():
    for i in subjects:
        if i[0] == check[1]:
            verify = True
            correctWord = i[1]
            break
        else:
            verify = False
    if verify == True:
        if int(check[2]) < 1 or int(check[2]) > 10:
            print('Introdu o notă validă!')
        else:
            cursor.execute(f"insert into proggress (subject, grade) values('{correctWord}', {check[2]});")
            connection.commit()
            print('Adăugat cu success!')
    else:
        if verify == False:
            print('Introdu o lecție validă!')
        else:
            print('Nu am înțeles comanda!')

while True:
    ids = []
    num = 0
    all_avg_rating = ''
    subject_avg = []

    x = input('Beaver> ')

    check = x.split(' ')

    if x == 'exit':
        break

    if x == 'help':
        print('------------------------------------------------')
        print('help subjects - arată lista codurilor articol')
        print('show - arată o listă de note')
        print('show avg - arată media totală')
        print('show group - arată media fiecăror obiecte')
        print('add [Cod subject] [nota] - inrtoduceți ceva')
        print('update [id] [nota nouă] - actualizați evaluarea')
        print('del [id] - ștergeți o intrare')
        print('exit - ieșire')
        print('------------------------------------------------')

    elif check[0] == 'help':
        if check[1] == 'subjects':
            print('------------------------------------------------')
            print('Coduri Articol:')
            print('informatica')
            print('biologia')
            print('engleza')
            print('matematica')
            print('chimia')
            print('romana')
            print('fizica')
            print('istoria')
            print('rusa')
            print('tehnologica')
            print('geografia')
            print('muzica')
            print('sănătatea')
            print('------------------------------------------------')

        else:
            print('Nu am înțeles comanda!')
    elif x == 'show':
        cursor.execute('select * from proggress;')
        data = cursor.fetchall()
        if len(data) == 0:
            print('Nu exista date!')
        else:
            for i in data:
                print(f'Id = {i[0]}, Subject = {i[1]}, Nota = {i[2]}')

    elif check[0] == 'show':
        verify()
        if verifyShow == True:
            if check[1] == 'avg':
                cursor.execute('select avg(grade) from proggress;')
                h = cursor.fetchall()
                if h[0][0] == None:
                    print('Nu există date!')
                else:
                    all_avg_rating = str(h[0][0])
                    print(f'Media tuturor notelor este: {all_avg_rating[:4]}')
            elif check[1] == 'group':
                cursor.execute('select subject, avg(grade) from proggress group by subject;')
                j = cursor.fetchall()
                if len(j) == 0:
                    print('Nu există date!')
                else:
                    for i in j:
                        subject_avg.append(i)
                    for k in j:
                        num += 1
                        nota = str(k[1])
                        print(f'Subject = {k[0]}, Media = {nota[:4]}')
        else:
            print('Nu am înțeles comanda!')

    elif check[0] == 'add':
        add()

    elif check[0] == 'update':
        cursor.execute('select * from proggress;')
        data = cursor.fetchall()

        cursor.execute('select id from proggress;')
        Ids = cursor.fetchall()

        if len(data) == 0:
            print('Nu exista date!')
        else:
            for i in Ids:
                ids.append(i[0])
                num += 1
            if int(check[1]) in ids:
                if int(check[2]) < 1 or int(check[2]) > 10:
                    print('Introdu o notă validă!')
                else:
                    cursor.execute(f"UPDATE proggress SET grade = {check[2]} WHERE id = {check[1]};")
                    connection.commit()
                    print('Nota schimbată cu succes!')
            else:
                print(f'Nu este nici un subiect cu ID-ul {check[1]}!')

    elif check[0] == 'del':
        cursor.execute('select * from proggress;')
        data = cursor.fetchall()

        cursor.execute('select id from proggress;')
        Ids = cursor.fetchall()

        if len(data) == 0:
            print('Nu exista date!')
        else:
            for i in Ids:
                ids.append(i[0])
                num += 1
            if int(check[1]) in ids:
                everyData = []
                cursor.execute(f"delete from proggress where id = '{check[1]}';")
                connection.commit()
                cursor.execute(f"select * from proggress;")
                everyData = cursor.fetchall()
                cursor.execute(f"drop table proggress")
                connection.commit()
                create = '''create table if not exists proggress(
                             id integer primary key autoincrement,
                             subject text,
                             grade integer);
                         '''
                cursor.execute(create)
                connection.commit()
                for i in everyData:
                    cursor.execute(f"insert into proggress (subject, grade) values('{i[1]}', {i[2]});")
                connection.commit()
                print(f'Id-ul {check[1]} șters cu succes!')
            else:
                print(f'Nu este nici un subiect cu ID-ul {check[1]}!')
    else:
        print('Nu am înțeles comanda!')

connection.close()