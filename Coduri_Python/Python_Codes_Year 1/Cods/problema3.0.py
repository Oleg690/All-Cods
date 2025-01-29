import random
x = []
while len(x) < 5:
    y = random.randint(0,9)
    if not y in x:
        x.append(y)
print(x)