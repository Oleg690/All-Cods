list1 = [5, 10, 15, 20, 35, 25, 15, 20, 68]

for i in range(len(list1)):
    if list1[i] == list1[3]:
        list1[i] = 200
print(list1)