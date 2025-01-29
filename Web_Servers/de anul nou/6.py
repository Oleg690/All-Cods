x = input('Introduceți numărul zilei: ')
y = input('Introduceți numărul lunii: ')

if x == '1' and y == '1':
    print('An Nou fericit!')
elif y == '12' and x >= '15':
    print('Vine Anul Nou!')
else:
    zile = 0
    lunile_cu_zile = [
    '31',
    '28',
    '31',
    '30',
    '31',   
    '30',
    '31',
    '31',
    '30',
    '31',
    '30',
    '31']

    for i in lunile_cu_zile[int(y)-1:12]:
        zile += int(i)
    zile -= int(x)
    print(f'Zile rămase până la anul nou: {zile}')