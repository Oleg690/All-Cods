x = input('Introduceti o propozitie cu numere: ')

result = ''

for i in x:
    if i.isdigit() == True:
        i = int(i)
        i += 1
        result += str(i)
    else:
        result += i

print(result)