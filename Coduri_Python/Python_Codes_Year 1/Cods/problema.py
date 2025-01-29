while True:
    parola = input('Introduceti parola: ')
    if len(parola) < 6:
        print('Parola trebuie sa fia cu mai mult de 6 caractere! Nu e setata!')
        continue
    elif ' ' in parola:
        print('Parola nu trebuie sa contina spatii! Nu e setata!')
        continue
    elif parola.isdigit() == True or parola.isalpha() == True:
        print('Parola trebuie să conțină litere și cifre. Nu e setata!')
    elif parola == parola.upper() or parola == parola.lower():
        print('Parola trebuie sa contina litere mici si mari! Nu a fost setata!')
        continue
    else:
        print('Parola este setata.')
        break