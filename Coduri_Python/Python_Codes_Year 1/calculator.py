import tkinter
from tkinter import messagebox

master = tkinter.Tk()
master.title('Calculator')
master.geometry('300x300')
widget_font = ('Arial', 12, 'bold')

num1 = tkinter.StringVar()
num2 = tkinter.StringVar()
symbol = tkinter.StringVar()
result = tkinter.StringVar()

num1_label = tkinter.Label(text='Introduceti prima cifra: ', font=widget_font)
num1_label.place(x=50, y=20)

num1_entry = tkinter.Entry(textvariable=num1, width=22, font=widget_font)
num1_entry.place(x=50, y=50)

num2_label = tkinter.Label(text='Introduceti a doua cifra: ', font=widget_font)
num2_label.place(x=50, y=80)

num2_entry = tkinter.Entry(textvariable=num2, width=22, font=widget_font)
num2_entry.place(x=50, y=110)

symbol_label = tkinter.Label(text='Introduceti simbolul: ', font=widget_font)
symbol_label.place(x=50, y=140)

symbol_entry = tkinter.Entry(textvariable=symbol, width=22, font=widget_font)
symbol_entry.place(x=50, y=170)

result_label = tkinter.Label(text=result, font=widget_font)
result_label.place(x=50, y=200)

def btn1():
    if symbol == '+':
        result = int(num1) + int(num2)
    elif symbol == '-':
        result = int(num1) - int(num2)
    elif symbol == '*':
        result = int(num1) * int(num2)
    elif symbol == '/':
        result = int(num1) / int(num2)


btn1 = tkinter.Button(text=result, command=btn1, width=8, font=widget_font)
btn1.place(x=20, y=150)

master.mainloop()