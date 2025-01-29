x = input('Introduceti niste : ')
mari = []
mici = []
for i in x:
    if i.isalpha():    
        if i.isupper():
            mari.append(i)
        else:
            mici.append(i)
    else:
        pass

print('Litere mari: ', len(mari))
print('Litere mici: ', len(mici))