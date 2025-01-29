import tkinter
from tkinter import messagebox
import createFile
import Authorization

master = tkinter.Tk()
master.title('Autentificare')
master.geometry('300x200')

widget_font = ('Arial', 12, 'bold')
login_var = tkinter.StringVar()
pass_var = tkinter.StringVar()

login_label = tkinter.Label(text='Introduceti login:', font=widget_font)
login_label.place(x=50, y=20)

login_entry = tkinter.Entry(textvariable=login_var, width=22,font=widget_font)
login_entry.place(x=50, y=50)

pass_label = tkinter.Label(text='Password:', font=widget_font)
pass_label.place(x=50, y=80)

pass_entry = tkinter.Entry(textvariable=pass_var, width=22,font=widget_font)
pass_entry.place(x=50, y=110)

def btn1click():
    login = login_var.get()
    if len(login) == 0:
        messagebox.showwarning('Warning', 'Loginul nu este setat!')
        return

    for i in range(len(login)):
        if login[i] != ' ':
            login = login[i:]
            break
    
    for i in range(len(login) - 1, -1, -1):
        if login[i] != ' ':
            login = login[:i+1]
            break

    login_var.set(login)

    password = pass_var.get()
    if len(password) == 0:
        messagebox.showwarning('Warning', 'Parola nu este setată!')
        return

    for i in range(len(password)):
        if password[i] != ' ':
            password = password[i:]
            break
    
    for i in range(len(password) - 1, -1, -1):
        if password[i] != ' ':
            password = password[:i+1]
            break

    pass_var.set(password)

    success, msg = Authorization.verify(login, password)

    if success:
        messagebox.showinfo('Intra', 'Bine ati venit!')
    else:
        messagebox.showwarning('Intra', msg)

def btn2click():
    master.destroy()

btn1 = tkinter.Button(text='Login', command=btn1click, width=8, font=widget_font)
btn1.place(x=20, y=150)

btn2 = tkinter.Button(text='Cancel', command=btn2click, width=8, font=widget_font)
btn2.place(x=180, y=150)

master.mainloop()