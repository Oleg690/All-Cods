import random
x = int(input('Introduceti cat de lunga sa fie lista: '))
result = []
for i in range(x):
    result.append(random.randint(1,9))
print(result)
    