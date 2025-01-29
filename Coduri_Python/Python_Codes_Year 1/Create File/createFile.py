import json
from tkinter import messagebox

def test_create_file():
    data = {}
    data['users'] = [['admin','123'],['user','111']]
    data['last_login'] = 'admin'
    x = open('data.txt', 'w', encoding='utf-8')
    json.dump(data, x, indent=4)
    text = json.dumps(data, indent=4)
    x.write(text)
    x.close()

def test_read_file():
    x = open('user.txt', 'r', encoding = 'utf-8')
    text = x.read()
    x.close

    messagebox.showinfo('Users.txt', text)


# w - write. Modul de inscriere. Creaza file daca nu il gaseste.
# r - read. Modul de citire. Daca file nu exista ne da eruare.
# r+w - Read and Write. Modul Modul de citire si inscriere.
        # Daca file nu exista, ne da error.