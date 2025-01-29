browser = input('Introduceti numele browser-ului:')
if len(browser) < 9:
    print(False)
if browser[:4] == 'www.' and\
(browser[-3]=='.' or browser[-4] == '.'):
    print(True)
else:
    print(False)