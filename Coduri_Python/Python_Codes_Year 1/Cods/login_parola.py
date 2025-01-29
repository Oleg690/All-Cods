import tkinter
from tkinter import messagebox

master = tkinter.Tk()
master.title('Autentificare')
master.geometry('300x200')

widget_font = ('Arial', 10, 'bold')
login_var = tkinter.StringVar()
password_var = tkinter.StringVar()

login_label = tkinter.Label(text='Introduceti login-ul:', font=widget_font)
login_label.place(x=50, y=20)

login_entry = tkinter.Entry(textvariable=login_var, width=28, font=widget_font)
login_entry.place(x=50, y=50)



password_label = tkinter.Label(text='Parola:', font=widget_font)
password_label.place(x=50, y=80)

password_entry = tkinter.Entry(textvariable=password_var, width=28, font=widget_font)
password_entry.place(x=50, y=110)

def btn1click():
    login = login_var.get()
    if len(login) == 0:
        messagebox.showwarning('Warning!','Trebuie să scrii cela la login!')
        return

    if ' ' in login:
        messagebox.showwarning('Warning!','Login-ul are spațiu liber')
        return

    messagebox.showinfo('Info','Bun venit!')

loginbtn1 = tkinter.Button(text='Login', command=btn1click, width=8)
loginbtn1.place(x=55, y=150)

def btn2click():
    master.destroy()

cancelbtn2 = tkinter.Button(text='Cancel', command=btn2click, width=8)
cancelbtn2.place(x=175, y=150)

master.mainloop()