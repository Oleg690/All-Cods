while True:
    x = input('Introduceti parola: ')
    if x == '':
        print('Nu ati scris numere!')
    elif x.isdigit() == False:
        print('Introduceți o valoare constând numai din cifre')
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
        break