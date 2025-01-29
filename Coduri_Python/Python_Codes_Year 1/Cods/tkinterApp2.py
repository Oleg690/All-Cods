import tkinter
master = tkinter.Tk()
master.title('Counter')
master.geometry('300x250')

value = 1

label = tkinter.Label(text = '1')
label.place(x = 150, y = 50)

def bnt1click():
    global value
    value +=1
    label['text'] = value

bnt1 = tkinter.Button(text = 'Press', command = bnt1click)
bnt1.place(x = 138, y = 75)

master.mainloop()