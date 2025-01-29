x = input('Introduceti parola: ')
if x == '':
    print('Nu ati scris nimic!')
else:
    resultat = True
    origin = []
    for i in x:
        if not i in origin:
            origin.append(i)
        else:
            resultat = False
            break
    print(resultat)
    print(origin)