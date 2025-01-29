x = input('Introduceti o propozitie: ')
result = ''
count_space = 0
for i in x:
    if i == ' ':
        if count_space == 0:
            result += i
            count_space = 1
    else:
        result += i
        count_space = 0
print(result)