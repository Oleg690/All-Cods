import random

numbers = []

list_plus = []
list_minus = []

for i in range(10):
    numbers.append(random.randint(-10, 10))


for i in numbers:
    if i > 0:
        list_plus.append(i)
    else:
        list_minus.append(i)

print('Pozitive:', len(list_minus))
print('Negative', len(list_plus))

if len(list_plus) < len(list_minus):
    print('Avem mai multe pozitive')
elif len(list_plus) == len(list_minus):
    print('Nimeni nu a castigat!')
else:
    print('Avem mai multe negative')