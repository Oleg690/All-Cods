import json

data = {}
data['1:4'] = 500
data['5:8'] = 350

print('Keys: ')

for i in data:
    print(i)

print('Values:')

for i in data:
    print(data[i])

x = '1:4'
y = x.split(':')
print(y)

#Inscrie
file = open('Repetare json\data.txt', 'w', encoding='utf-8')
json.dump(data, file, indent=4)
file.close()

#Citire
file = open('Repetare json\data.txt', 'r', encoding='utf8')
data = json.load(file)
file.close()

print(data)