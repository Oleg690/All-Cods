import tkinter
import random

master = tkinter.Tk()
master.title("Hello")
canvas = tkinter.Canvas(width=1366, height=700, bg='lightgray')
widget_font = ('Arial', 50)
btn_font = ("Arial", 25)

def on_enter(event):
    x = random.randint(150,1210)
    y = random.randint(150,550)
    btn2.place(x=x, y=y)

def btn1():
    canvas.create_text(683, 500, text="Totuși știam! :))))", font=widget_font)

canvas.create_text(683, 50, text="Esti gay?", font=widget_font)

btn1 = tkinter.Button(text="Da", command=btn1, width=8, font=btn_font, fg='#6d6d6d')
btn1.place(x=400, y=200)

btn2 = tkinter.Button(text="Nu", command=on_enter, width=8, font=btn_font, state="disabled")
btn2.place(x=800, y=200)

btn2.bind("<Enter>", on_enter)
canvas.pack()
master.mainloop()