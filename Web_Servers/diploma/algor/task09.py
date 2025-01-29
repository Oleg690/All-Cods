x = input("Introduceti sirul de cifre: ")

maxNum = 0

for i in str(x):
    if int(i) > maxNum:
        maxNum = int(i)

counter = maxNum

strInput = str(x)
intInput = int(x)

length = len(strInput)

for i in range(maxNum):
    result = ''
    
    for k in strInput:
        if int(k) >= counter:
            result += '*'
        else:
            result += ' '

    counter -= 1

    print(result)
