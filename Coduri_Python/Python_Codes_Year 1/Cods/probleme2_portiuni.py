x = input('Introduceti un numere: ')
resultat = False
for i in x:
    if int(i) >= 1 and int(i) <= 5:
        resultat = True
        break
print(resultat)
('1' in x)