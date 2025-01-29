counter = 0

for i in range(1, 1000000):
    counter = 0
    for j in range(1, 16):
        if i % j == 0:
            counter += 1
    if counter == 15:
        break
print(i)