x = input('Introduceti un enunt: ') # 2 + 2 = 4
result = ''
for i in x:
    if i.isdigit():
        result += str(int(i)+1)
    else:
        result += i
print(result)