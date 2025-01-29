import random

number_to_guess = random.randint(1, 50)
user_number = int(input('Introduceti un namar de la 1 la 50: '))

if user_number == number_to_guess:
    print('Ati castigat!!! Felicitari!')
else:
    print('Ati piardut si numarul care nu lati gicit este', number_to_guess,'.')

while user_number != 0:
    import random

    number_to_guess = random.randint(1, 5)
    user_number = int(input('Introduceti un namar de la 1 la 50: '))

    if user_number == number_to_guess:
        print('Ati castigat!!! Felicitari!')
    else:
        print('Ati piardut si numarul care nu lati gicit este', number_to_guess,'.')
    if user_number == 0:
        print('Bine, o sa ma opresc.')