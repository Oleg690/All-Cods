import tkinter
import subprocess

master = tkinter.Tk()
master.title('Main Page')

window_width = 500
window_height = 500
x_position = 500
y_position = 130

geometry_string = f"{window_width}x{window_height}+{x_position}+{y_position}"

master.geometry(geometry_string)
widget_font = ('Calibri', 18)

label = tkinter.Label(text='Hello', font=widget_font)
label.place(x=170, y=50)

master.mainloop()

#window_width = 400
#window_height = 450
#x_position = 500
#y_position = 130