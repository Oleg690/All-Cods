import json

data = {}

while True:
    x = int(input('Introduceti randul incapator: '))

    if x <= 0:
        break

    y = int(input('Introduceti randul de sfarsit: '))

    if y >= 16:
        break

    _range = f'{x}:{y}'

    if _range in data:
        print('Acest diapozon deja este setat')
        continue

    z = int(input('Introduceti costul biletului: '))

    data[_range] = z

file = open('Python Codes Year 2\Cinema\\txt\data.txt', 'w', encoding='utf-8')
json.dump(data, file, indent=4)
file.close()

print("Preturile au fost salvate in baza de date")