x = input('Introduceti un cuvant: ')
if len(x)<3:
    print('Cuvantul introdus este prea scurt.')
else:
    print(x[0] == 'M' or x[0] == 'm')