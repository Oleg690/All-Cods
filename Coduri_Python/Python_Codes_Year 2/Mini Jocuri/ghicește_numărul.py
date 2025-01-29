import random

y = input('Introduceți un numar: ')

if y.isdigit():
    y = int(y)

    if y <= 0:
        print('Introduceți un numar mai mare de 0.')
        quit()
else:
    print('Enter a number!!!')
    quit()

number = random.randint(0, y + 1)

print(f'Acum trebuie să alegeți ghiciți un numar de la 1 la {y} și aveți 3 încercări')

tries = 0
used_tries = 3

while True:
    tries += 1
    used_tries -= 1

    if tries <= 3:
        question = input(f'Introdu numărul: ')
        if int(question) < number:
            tries - 1
            print(f'Nu, numarul este mai mare, mai ai {used_tries} încercări')
        elif int(question) > number:
            tries - 1
            print(f'Nu, numarul este mai mic, mai ai {used_tries} încercări')
        else:
            print(f'Corect, numarul era {number}.')
            break
    else:
        print('Ai pierdut, nu mai ai încercări')
        break