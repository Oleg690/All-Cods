import random

odd = 0
even = 0

for i in range(1, 101):
    x = random.randint(1, 10)
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print('Impar:', odd)
print('Par:', even)

if odd > even:
    print('Impar a castigat!')
else:
    print('Par a castigat!')