x = input('Inroduceti niste numere: ')
count = []
for i in x:
    if i.isdigit():
        count.append(int(i))

print(sum(count))