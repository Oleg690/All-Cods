import tkinter
from tkinter import messagebox
import json

master = tkinter.Tk()
master.title('Calculator')
master.geometry('300x300')
widget_font = ('Arial', 12, 'bold')

num1 = tkinter.StringVar()
num2 = tkinter.StringVar()
symbol = tkinter.StringVar()
result = tkinter.StringVar()
result2 = ''

num1_label = tkinter.Label(text='Introduceți prima cifra: ', font=widget_font)
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

result_label = tkinter.Label(textvariable=result, font=widget_font)
result_label.place(x=50, y=230)

def btn1():
    global result
    if symbol.get() == '+':
        summa = int(num1.get()) + int(num2.get())
        result.set(summa)
    if symbol.get() == '-':
        summa = int(num1.get()) - int(num2.get())
        result.set(summa)
    if symbol.get() == '*':
        summa = int(num1.get()) * int(num2.get())
        result.set(summa)
    if symbol.get() == '/':
        summa = int(num1.get()) / int(num2.get())
        result.set(summa)



btn1 = tkinter.Button(text='Submit', command=btn1, width=8, font=widget_font)
btn1.place(x=50, y=200)

master.mainloop()

#file = open('Python Codes Year 1\Calculator\calculator_results.txt', 'w', encoding='utf-8')
#result2 = num1.get() + symbol.get() + num2.get() + '=' + result.get()
#json.dump(result2, file, indent=4)
#file.close()
print('Suncceasfuly loaded!')