o = 1
cadou = []
while True:
    x = input(f'Introduceți cadoul {str(o)}: ')
    o += 1
    if x == 'stop':
        z = 1
        print(f'Primește de la Moș Crăciun: ')
        for i in cadou:
            print(f'{z}. {i}')
            z+=1
        break
    elif x != '':
        cadou.append(x)