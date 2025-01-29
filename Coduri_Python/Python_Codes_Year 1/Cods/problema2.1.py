x = input('Introduceti niste numere: ')
result = []
y = x.split()
for i in x:
    if i.isdigit():
        result.append(int(i))
print(sum(result))
print(sum(result)/len(y))