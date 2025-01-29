import json

file = open('Python Codes Year 2\Cinema\\txt\data.txt', 'r', encoding='utf8')
data = json.load(file)
file.close()

while True:
    x = input('Introduceti randul: ')

    if x == '':
        continue

    if x == 'stop':
        break

    if int(x) <= 0 or int(x) >= 16:
        print('Numarul randului nu este valid!')
        continue

    price = 0

    for i in data:
        _range = i.split(':')
        begin = int(_range[0])
        end = int(_range[1])

        if int(x) >= int(begin) and int(x) <= int(end):
            price = data[i][0]
            break

    if price == 0:
        print(f'Pretul pentru randul {x} nu a fost gasit')
    else:
        print(f'Pretul biletului in radnul {x} este {price} lei')

print('')
print('Codul sa oprit')
print('')