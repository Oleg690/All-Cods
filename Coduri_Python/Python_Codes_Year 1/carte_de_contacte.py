import json
import os.path

if os.path.exists("Contact_list.txt"):
    file = open("Contact_list.txt", 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    print('Lista de contacte a fost incarcata!')
else:
    data = {}
    data['generator'] = 0
    data['contacts'] = {}

while True:
    action = int(input('Alegeti actiunea:(1-add),(2-edit),(3-del),(4-show),(0-exit): '))

    if action == 0:
        break
    elif action == 1:
        print('Adaugă contact:')
        name = input('Introdu numele abonatului: ')
        phone_number = input('Introdu numărul de telefon: ')
        
        data['generator'] += 1
        new_id = str(data['generator'])

        data[new_id] = [name, phone_number]

        contact_list = data['contacts']
        contact_list[new_id] = [name, phone_number]

        print('Contactul cu numele: "{}" ADĂUGAT'.format(name))

    elif action == 2:
        print('Edit:')
        id_contact = input('Introdu ID contact: ')

        contact_list = data['contacts']

        if not id_contact in contact_list:
            print('Contact cu ID = {} nu exista.'.format(id_contact))
            continue
        else:
            new_name = input('Introduceti numele persoanei: ')
            new_phone = input('Introdu numarul nou a abonatului: ')
            
            contact_list[id_contact] = [new_name, new_phone]

            print('Abonatul cu ID = {} a fost editat.'.format(id_contact))
    
    elif action == 3:
        print('Delete:')
        id_contact = input('Introdu ID contact: ')
        
        contact_list = data['contacts']

        if not id_contact in contact_list:
            print('Contact cu ID = {} nu exista.'.format(id_contact))
            continue
        else:
            del contact_list[id_contact]
            print('Contactul cu ID = {} a fost sters cu success.'.format(id_contact))

    elif action == 4:
        print('Contactele:')
        contact_list = data['contacts']
        for i in contact_list:
            value = data[i]
            print('ID = {}, nume = {}, telefon = {}'.format(i, value[0], value[1]))
            print()

file = open("Contact_list.txt", 'w', encoding='utf-8')
json.dump(data, file, indent=4)
file.close()
print('Lista de contacte a fost salvata!')

print('Ați ieșit din contacte!')