a = int(input('Introduceti un numar: '))
result = []
for i in range(a+1):
    result.append(i * i)
print(result)

#print([i*i for i in range(int(input('Introduceti un numar: '))+1)])