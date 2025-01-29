x = input('Introduceti 3 numere: ')
y = x.split(',')

for i in range(len(y)):
    y[i] = int(y[i])
print(y)

#a = int(y[0])
#b = int(y[1])
#c = int(y[2])
#if c < b:
#    b,c = c,b
#if b < a:
#    a,b = b,a
#if c < b:
#    c,b = b,c
#print(a,b,c)

