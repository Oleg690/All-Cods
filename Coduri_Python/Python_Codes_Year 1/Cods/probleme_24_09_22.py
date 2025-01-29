result = []
while True:
    x = input('Introduceti niste numere: ')
    if x == 'end':
        break
    if int(x) % 2 == 0:
        result.append(int(x))
print(result)