import tkinter
master = tkinter.Tk()
master.title('Counter')
master.geometry('300x250')

entry_var = tkinter.StringVar()

entry1 = tkinter.Entry(textvariable = entry_var, width = 10)
entry1.place(x = 80, y = 60)

entry_var2 = tkinter.StringVar()

entry2 = tkinter.Entry(textvariable = entry_var2, width = 10)
entry2.place(x = 160, y = 60)

def bnt1click():
    entry_varm = entry_var.get()
    entry_var.set(entry_var2.get())
    entry_var2.set(entry_varm)

bnt1 = tkinter.Button(text = 'Press', command = bnt1click)
bnt1.place(x = 137, y = 85)

master.mainloop()