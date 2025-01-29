x = input('Introduceti o lista de litere mici si mari: ')
mari = 0
mici = 0
for i in x:
    if i.isupper():
        mari +=1
    else:
        mici +=1
print('Litere mari: ', mari)
print('Litere mici: ', mici)