import random
x = int(input('Introduceti cat de lunga sa fie lista: '))
result1 = []
for i in range(x):
    result1.append(random.randint(0,9))
result2 = []
for i in range(1,len(result1)):
    if result1[i] > result1[i-1]:
        result2.append(result1[i])
print(result1)
print(result2)