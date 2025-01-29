counter = 0
counterForThree = 0

for i in range(1, 1000):
    i = str(i)
    if i.count('3') >= 2:
        counter += 1
        print(i)


print(counter)