luni = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']
x = input('Data: ')
y = x.split('.')
ziua = y[0]
if ziua[0] == '0':
    ziua = ziua[1]
print(ziua+'.'+luni[int(y[1])-1]+'.'+y[2])