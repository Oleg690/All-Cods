x = input('Scrieti cuvantul: ')
result = ''
for i in range(1,len(x)+1):
    result += x[-i]
print(result)