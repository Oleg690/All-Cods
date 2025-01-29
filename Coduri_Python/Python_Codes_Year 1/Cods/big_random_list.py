import random

count_plus = 0
count_minus = 0

odd = 0 # impar
even = 0 # par
result = 0



x = []
for i in range(10):
    random_number = x.append(random.randint(-10, 10))# append = a adauga

for num in x:
    result = result + num
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    if num > 0:
        count_plus = count_plus + 1
    else:
        count_minus = count_minus + 1

print(x)
print('Numere pozitive:', count_plus)
print('Numere negative:', count_minus)
print('Par', even)
print('Impar', odd)
print('Valoarea medie:', result / 10)
print('Numarul maxim:', max(x))
print('Numarul minim:', min(x))