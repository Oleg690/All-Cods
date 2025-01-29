import tkinter 
master = tkinter.Tk()
master.title('Generator')
master.geometry('600x600')

entry_list = []

def btn1click():
    global entry_list

    for i in entry_list:
        i.destroy()

    entry_list = []

    count = int(var1.get())

    for i in range(count):
        x = tkinter.Entry(width = 5)
        left = 20 + i * 40
        x.place(x=left, y=100)
        entry_list.append(x)

var1 = tkinter.StringVar()
var1.set(0)
entry1 = tkinter.Entry(textvariable = var1, width = 5)
entry1.place(x=30,y=30)

bnt1 = tkinter.Button(text = 'Button', command = btn1click)
bnt1.place(x=80,y=30)

master.mainloop()