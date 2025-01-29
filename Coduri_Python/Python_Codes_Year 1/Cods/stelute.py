#x = input('Introduceti niste numere: ')
#for i in x:
#    if i == ' ':
#        pass
#    else:
#        print('*'*int(i))

x = input('Introduceti niste numere: ')
y = x.split()
for i in y:
    print('*'*int(i))