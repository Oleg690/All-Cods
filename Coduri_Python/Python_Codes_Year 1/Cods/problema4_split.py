luni = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']
x = input('Data: ')
y = x.split('.')
print(y[0]+'.'+luni[int(y[1])-1]+'.'+y[2])