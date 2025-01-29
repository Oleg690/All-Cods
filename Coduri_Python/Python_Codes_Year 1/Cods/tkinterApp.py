import tkinter
master = tkinter.Tk()
master.title('Window App')
master.geometry('300x250')

label = tkinter.Label(text = 'I\'m Label')
label.place(x = 20, y = 20)

entry_var = tkinter.StringVar()

entry1 = tkinter.Entry(textvariable = entry_var, width = 40)
entry1.place(x = 20, y = 60)

def bnt1click():
    label['text'] = 'Hello world!'

bnt1 = tkinter.Button(text = 'Change label', command = bnt1click)
bnt1.place(x = 20, y = 100)

def btn2click():
    entry_var.set('New Value')

btn2 = tkinter.Button(text = 'Set Value Entry', command = btn2click)
btn2.place(x = 20, y = 140)

def btn3click():
    label['text'] = entry_var.get()

btn3 = tkinter.Button(text = 'Read Value', command = btn3click)
btn3.place(x = 20, y = 180)

master.mainloop()