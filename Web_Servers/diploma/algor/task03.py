firstRow = 1
secondRow = 1

for i in range(1, 11):
    if firstRow == 11:
        break

    for i in range(1, 11):
        print(f'{firstRow}x{secondRow}={firstRow*secondRow}')
        secondRow += 1
        
    secondRow = 1
    firstRow += 1