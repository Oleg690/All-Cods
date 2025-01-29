x = input('Introduceti parola: ')
resultat = True
origin = []
for i in x:
    if not i in origin:
        origin.append(i)
    else:
        resultat = False
        break
print(resultat)
print(origin)