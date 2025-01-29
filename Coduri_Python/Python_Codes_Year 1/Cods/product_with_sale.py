result = 0

while True:
    price = int(input('Introducei pretul: '))
    if price == 0:
        break
    elif price < 0:
        print('Pretul nu poate sa fie mai mic ca 0.')
        continue
    
    if price > 500:
        result += price * 0.9

    else: 
        result += price


print('Suma', result)