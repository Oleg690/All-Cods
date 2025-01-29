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
    row = int(var1.get())
    col = int(var2.get())

    for i in range(row):     
        x = tkinter.Entry(width = 5)
        left = 20 + i * 40
        x.place(x=left, y=100)
        entry_list.append(x)

    for i in range(col):
        x = tkinter.Entry(width = 5)
        up = 20 + i * 40
        x.place(x=30, y=up)
        entry_list.append(x)



var1 = tkinter.StringVar()
var1.set(0)

label_row = tkinter.Label(text='Row:')
label_row.place(x=30,y=30)

entry1 = tkinter.Entry(textvariable = var1, width = 5)
entry1.place(x=65,y=31)

var2 = tkinter.StringVar()
var2.set(0)

label_col = tkinter.Label(text = 'Col:')
label_col.place(x=100,y=30)

entry2 = tkinter.Entry(textvariable = var2, width = 5)
entry2.place(x=130,y=30)

bnt1 = tkinter.Button(text = 'Button', command = btn1click)
bnt1.place(x=170,y=27)



master.mainloop()