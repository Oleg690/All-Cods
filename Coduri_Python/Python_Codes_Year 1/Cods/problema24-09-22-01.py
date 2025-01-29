x = input('Introduceti niste numere separate prin spatiu: ')
y = x.split(' ')
result = []
for i in range(int(y[0])+1,int(y[1])):
    result.append(i*i)
print(result)