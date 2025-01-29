x = input('Introduceti niste : ')
mari = []
mici = []
rest = []
for i in x:
    if i.isalpha():    
        if i.isupper():
            mari.append(i)
        else:
            mici.append(i)
    else:
        rest.append(i)
print('Litere mari: ', len(mari))
print('Litere mici: ', len(mici))
print('Rest: ', len(rest))