o = 1
cadou1 = ''
for i in range(1, 4):
    x = input(f'Introduceți cadoul {o}: ')
    if x != '':
        if o == 3:
            cadou1 += x
        else:
            cadou1 += x + ', '
    else:
        cadou1 += ''
    o += 1

print(f'Primește de la Moș Crăciun: {cadou1}')