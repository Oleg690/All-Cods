colors = ['red', 'green', 'yellow']

while True:
    action = int(input('Ce ati dori sa faceti cu aceasta lista? 1 - adaugati, 2 - stergeti.'))
    color = input('Ce culoare?')
    if action == 1:
        colors.append(color)
    elif action == 2:
        if color not in colors:
            print('Aceasta culoare nu este in lista noastra.')
            continue
        else:    
            colors.remove(color)
    elif action == 0:
        print('Ati iesit din program')
        break

print('Aici sunt toate culorile:')
for color in colors:
    print(color)