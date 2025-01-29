x = int(input('Introduceti un numar: '))

counter = 2

for i in range(2, x):
    if x % i != 0:
        counter += 1
        if counter == x-1:
            print('Numarul este simplu')
            break
    else:
        print('Numarul este compus')
        break