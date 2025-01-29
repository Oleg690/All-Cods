x = input('Introduceti un cuvant: ')
if len(x)<3:
    print('Cuvantul introdus este prea scurt.')
elif x[0].isupper() and x[0] == 'M':
    print(True)
else:
    print(False)