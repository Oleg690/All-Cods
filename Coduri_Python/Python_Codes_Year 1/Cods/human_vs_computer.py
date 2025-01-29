import random

x = random.randint(1, 2)

human = 0
computer = 0

for i in range(1, 4):
    print('Incercarea nr.', i)
    y = int(input('Introduceti 1 sau 2: '))

    if x == y:
        print('Ati castigat! + 1 punct!')
        human = human + 1
    else:
        print('A castigat calculatorul! + 1 punct lui!')
        computer = computer + 1

print('Scorul omului:', human, 'Scorul calculatorului:', computer)

if human > computer:
    print('A castigat omul!')
else:
    print('A castigat calculatorul!')