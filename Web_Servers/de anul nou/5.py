x = input('Introduceți numărul zilei: ')
y = input('Introduceți numărul lunii: ')

if x == '1' and y == '1':
    print('An Nou fericit!')
elif y == '12' and x >= '15':
    print('Vine Anul Nou!')
else:
    print('Bună ziua!')