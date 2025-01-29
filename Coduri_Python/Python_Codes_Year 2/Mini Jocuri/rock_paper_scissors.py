import random

data = ['Foarfece', 'Piatră', 'Hârtie']
human = 0
computer = 0
human_guess = ''

print('Alege foarfecă, hârtie, sau piatră: ')


while True:
    guess = input('Alege 1 - foarfecă, 2 - piatră, 3 - hârtie, 0 - ieșire: ')

    if guess.isdigit():
        guess = int(guess)
        if guess < 0 or guess > 3:
            print('Alege unul dintre numerele date!!!')
            continue
    else:
        print('Alege un număr!!!')
        continue

    comp_guess = random.choice(data)

    if guess == 0:
        break
    elif guess == 1:
        human_guess = 'Foarfece'
    elif guess == 2:
        human_guess = 'Piatră'
    elif guess == 3:
        human_guess = 'Hârtie'

    print(f'Omul a ales {human_guess}')
    print(f'Calculatorul a ales {comp_guess}')

    if human_guess == comp_guess:
        print('Egalitate')
    elif human_guess != comp_guess:
        if human_guess == 'Foarfece' and comp_guess == 'Piatră':
            print('Calculatorul a câștigat')
            computer += 1
        if human_guess == 'Foarfece' and comp_guess == 'Hârtie':
            print('Omul a câștigat')
            human += 1
        if human_guess == 'Piatră' and comp_guess == 'Foarfece':
            print('Omul a câștigat')
            human += 1
        if human_guess == 'Piatră' and comp_guess == 'Hârtie':
            print('Calculatorul a câștigat')
            computer += 1
        if human_guess == 'Hârtie' and comp_guess == 'Foarfece':
            print('Calculatorul a câștigat')
            computer += 1
        if human_guess == 'Hârtie' and comp_guess == 'Piatră':
            print('Omul a câștigat')
            human += 1

if human < computer:
    print(f'Calculatorul a câștigat omul {computer} la {human}')
else:
    print(f'Omul a câștigat calculatorul {human} la {computer}')