import random

x = []

for i in range(5):
    y = random.randint(2, 11)
    x.append(y)

minNum = 11

for i in x:
    if i < minNum:
        minNum = i

maxNum = 0

for i in x:
    info = 0
    if i > maxNum:
        maxNum = i

itemsValue = 0

for i in x:
    itemsValue += i

avgNum = itemsValue / len(x)

print('Note in jurnal:', x)

print('Note maximala in jurnal:', maxNum)
print('Note minim in jurnal:', minNum)
print('Note medie in jurnal:', avgNum)