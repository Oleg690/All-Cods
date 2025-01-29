x = input('Introduceti o propozitie: ')

result = x[0]

for i in range(1, len(x)):
    char = x[i]
    pri_char = x[i-1]

    if x[i] == x[-1]:
        suc_char = x[i]
    else:
        suc_char = x[i]

    if pri_char != ' ':
        if suc_char != ' ':
            result += '-'

    result += char

print(result)