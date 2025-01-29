import sqlite3

file = open('airports.csv', 'r', encoding='utf-8')
data = file.read()
file.close()

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

sql = '''
create table if not exists airports (
name_rus text,
name_eng text,  
city_rus text,
city_eng text,
gmt_offset text,
country_rus text,
phone text,
email text,
website text
)
'''

cursor.execute(sql)

connection.commit()

rows = data.split('\n')

def getValue(x):
    if x != '':
        return '"' + x + '"'
    else:
        return 'NULL'

for i in range(1, len(rows)):
    row = rows[i]

    x = row.split(';')

    name_rus = getValue(x[0])
    name_eng = getValue(x[1])
    city_rus = getValue(x[2])
    city_eng = getValue(x[3])
    gtm_offset = getValue(x[4])
    country_rus= getValue(x[5])
    phone = getValue(x[6])
    email = getValue(x[7])
    website = getValue(x[8])

    sql = '''insert into airports values(
    {},{},{},{},{},{},{},{},{})'''.format(
        name_rus, name_eng, city_rus, city_eng, 
        gtm_offset, country_rus, phone, email, website
    )

    cursor.execute(sql)

connection.commit()
connection.close()

print("Complete!!!")