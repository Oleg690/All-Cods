x = int(input('Introduceti inaltimea bradului: '))

count = 1

for i in range(x):
    print((' '* (x - i - 1)) + ('*' * count))
    count += 2

print((' ' * (x - 1)) + '|')