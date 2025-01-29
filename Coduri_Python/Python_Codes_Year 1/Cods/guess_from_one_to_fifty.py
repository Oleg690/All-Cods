import random

number_to_guess = random.randint(1, 50)

chances = 5

while chances != 0:
    user_number = int(input('Introduceti un namar de la 1 la 50: '))
    if user_number > number_to_guess:
        chances = chances - 1
        print('Numarul este prea mare. Introduceti un numar mai mic.')
    elif user_number < number_to_guess:
        chances = chances - 1
        print('Numarul este prea mic. Introduceti un numar mai mare.')
    elif user_number == number_to_guess:
        print('Ati castigat! Felicitari!')
        break