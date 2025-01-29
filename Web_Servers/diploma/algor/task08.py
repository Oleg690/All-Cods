x = int(input("Introduceti dimensiunea: "))

fulgi = '* * * * *'

counter = 0

for i in range(x):
    counter += 1
    if counter % 2 != 0:
        print(f'{fulgi}')
    else:
        print(f'{' ' + fulgi}')