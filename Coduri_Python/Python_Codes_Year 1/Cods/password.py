while True:
    password = input('Introduceti parola: ')

    if ' ' in password:
        print('Parola nu poate sa contina nici un spatiu!')
        continue

    if len(password) < 6:
        print('Parola nu poate sa fie mai mica de 6 simboluri!')
        continue
    
    print('Parola este setata!')
    break